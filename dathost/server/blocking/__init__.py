from __future__ import annotations
from typing import Generator, Tuple, TYPE_CHECKING, cast

from ..base import ServerBase

from ...models.server import ServerModel
from ...models.file import FileModel
from ...models.backup import BackupModel
from ...models.metrics import MetricsModel
from ...models.match import MatchModel, MatchSeriesModel

from ...match.blocking import BlockingMatch, BlockingSeries

from .backup import BlockingBackup
from .file import BlockingFile

from ...settings import ServerSettings, MatchSettings, MatchSeriesSettings

from ...exceptions import InvalidConsoleLine

from ...routes import SERVER, MATCHES, MATCH_SERIES

if TYPE_CHECKING:
    from ... import Blocking


class ServerBlocking(ServerBase):
    _context: "Blocking"

    def create_match(self, match_settings: MatchSettings,
                     ) -> Tuple[MatchModel, BlockingMatch]:
        """Creates a match.

        Parameters
        ----------
        match_settings : MatchSettings
            Holds details on the match.

        Returns
        -------
        MatchModel
            Holds match details.
        BlockingMatch
            Used to interact with a match.
        """

        data = cast(
            dict,
            self._context._post(
                MATCHES.create,
                data={
                    "game_server_id": self.server_id,
                    **match_settings.payload
                },
                read_json=True
            )
        )

        return MatchModel(data), BlockingMatch(self._context, data["id"])

    def create_series(self, match_settings: MatchSeriesSettings,
                      ) -> Tuple[MatchSeriesModel, BlockingSeries]:
        """Creates a match.

        Parameters
        ----------
        match_settings : MatchSeriesSettings
            Holds details on the match series.

        Returns
        -------
        MatchModel
            Holds match details.
        BlockingSeries
            Used to interact with a series.
        """

        data = cast(
            dict,
            self._context._post(
                MATCH_SERIES.create,
                data={
                    "game_server_id": self.server_id,
                    **match_settings.payload
                },
                read_json=True
            )
        )

        return (
            MatchSeriesModel(data),
            BlockingSeries(self._context, data["id"])
        )

    def delete(self) -> None:
        """Used to delete a sever.
        """

        self._context._delete(
            SERVER.delete.format(self.server_id),
        )

    def get(self) -> ServerModel:
        """Used to get details on server.

        Returns
        -------
        ServerModel
            Holds data on server.
        """

        return ServerModel(
            cast(dict, self._context._get(SERVER.get.format(self.server_id)))
        )

    def update(self, settings: ServerSettings) -> None:
        """Update servers paramters.

        Parameters
        ----------
        settings : ServerSettings
            Used to configure server.
        """

        self._context._put(
            SERVER.update.format(self.server_id),
            data={
                **settings.payload,
                "server_id": self.server_id
            }
        )

    def console_send(self, line: str) -> None:
        """Used to send a command to console.

        Parameters
        ----------
        line : str
            Console command.
        """

        self._context._post(
            url=SERVER.console.format(self.server_id),
            data={
                "line": line,
            }
        )

    def console_retrive(self, lines: int = 1000) -> list:
        """Used to retrive lines from the console.

        Parameters
        ----------
        lines : int, optional
            Amount of lines to retrive, by default 1000

        Returns
        -------
        list
            List of strings.

        Raises
        ------
        InvalidConsoleLine
            Raised when console lines below 1 or above 100000.
        """
        if lines < 1 or lines > 100000:
            raise InvalidConsoleLine()

        data = cast(
            dict,
            self._context._get(
                url=SERVER.console.format(self.server_id),
                params={
                    "max_lines": lines,
                },
            )
        )

        return data["lines"]

    def sync(self) -> None:
        """Used to sync files from server to cache.
        """

        self._context._post(
            url=SERVER.sync.format(self.server_id)
        )

    def duplicate(self, sync: bool = False,
                  ) -> Tuple[ServerModel, ServerBlocking]:
        """Used to duplicate a server.

        Parameters
        ----------
        sync : bool
            Used to force update server cache, by default False

        Returns
        -------
        ServerModel
            Holds server data.
        ServerBlocking
            Used to interact with server.
        """

        if sync:
            self.sync()

        data = cast(
            dict,
            self._context._post(
                url=SERVER.duplicate.format(self.server_id),
                read_json=True,
            )
        )

        return ServerModel(data), ServerBlocking(self._context, data["id"])

    def ftp_reset(self) -> None:
        """Resets the FRP password.
        """

        self._context._post(
            url=SERVER.ftp.format(self.server_id)
        )

    def stop(self) -> None:
        """Used to stop the server.
        """

        self._context._post(
            url=SERVER.stop.format(self.server_id),
        )

    def start(self, allow_host_reassignment: bool = True) -> None:
        """Used to stop the server.

        Parameters
        ----------
        allow_host_reassignment : bool, optional
            By default True
        """

        self._context._post(
            url=SERVER.start.format(self.server_id),
            data={"allow_host_reassignment": allow_host_reassignment}
        )

    def reset(self) -> None:
        """Used to reset the server.
        """

        self._context._post(
            url=SERVER.reset.format(self.server_id),
        )

    def files(self, hide_default: bool = False, path: str = None,
              file_sizes: bool = False,
              deleted_files: bool = False
              ) -> Generator[Tuple[FileModel, BlockingFile], None, None]:
        """Used to list files.

        Parameters
        ----------
        hide_default : bool, optional
            by default False
        path : str, optional
            Path to use as root, by default None
        file_sizes : bool, optional
            by default False
        deleted_files : bool, optional
            Include deleted files in list, by default False

        Yields
        ------
        FileModel
            Holds details on a file.
        BlockingFile
            Used to interact with a file.
        """

        data = cast(
            dict,
            self._context._get(
                SERVER.files.format(self.server_id),
                params={
                    "hide_default_files": hide_default,
                    "path": path,
                    "with_filesizes": file_sizes,
                    "include_deleted_files": deleted_files
                },
            )
        )

        for file_ in data:
            yield FileModel(file_), self.file(file_["path"])

    def file(self, pathway: str) -> BlockingFile:
        """Used to interact with a file on the server.

        Parameters
        ----------
        pathway : str
            Pathway of file on server.

        Returns
        -------
        BlockingFile
        """

        return BlockingFile(
            self._context,
            self.server_id,
            pathway
        )

    def backups(self
                ) -> Generator[Tuple[BackupModel, BlockingBackup], None, None]:
        """Used to list backups a server has.

        Yields
        -------
        BackupModel
            Holds details on backup.
        Backup
            Used for interacting with a backup.
        """

        data = cast(
            dict,
            self._context._get(
                SERVER.backups.format(self.server_id),
            )
        )

        for backup in data:
            yield BackupModel(backup), self.backup(backup["name"])

    def backup(self, backup_name: str) -> BlockingBackup:
        """Used to interact with a backup.

        Parameters
        ----------
        backup_name : str
            Name of backup.

        Returns
        -------
        BlockingBackup
        """

        return BlockingBackup(
            self._context,
            self.server_id,
            backup_name
        )

    def metrics(self) -> MetricsModel:
        """Used to get server metrics.

        Returns
        -------
        MetricsModel
            Holds details on server metrics.
        """

        data = cast(
            dict,
            self._context._get(
                SERVER.metrics.format(self.server_id)
            )
        )

        return MetricsModel(data)
