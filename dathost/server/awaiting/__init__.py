from __future__ import annotations
from typing import AsyncGenerator, Tuple, TYPE_CHECKING, cast

from ..base import ServerBase

from ...models.server import ServerModel
from ...models.file import FileModel
from ...models.backup import BackupModel
from ...models.metrics import MetricsModel
from ...models.match import MatchModel, MatchSeriesModel

from ...match.awaiting import AwaitingMatch, AwaitingSeries

from .backup import AwaitingBackup
from .file import AwaitingFile

from ...settings import ServerSettings, MatchSettings, MatchSeriesSettings

from ...exceptions import InvalidConsoleLine

from ...routes import SERVER, MATCHES, MATCH_SERIES

if TYPE_CHECKING:
    from ... import Awaiting


class ServerAwaiting(ServerBase):
    _context: "Awaiting"

    async def create_match(self, match_settings: MatchSettings,
                           ) -> Tuple[MatchModel, AwaitingMatch]:
        """Creates a match.

        Parameters
        ----------
        match_settings : MatchSettings
            Holds details on the match.

        Returns
        -------
        MatchModel
            Holds match details.
        AwaitingMatch
            Used to interact with a match.
        """

        data = cast(
            dict,
            await self._context._post(
                MATCHES.create,
                data={
                    "game_server_id": self.server_id,
                    **match_settings.payload
                },
                read_json=True
            )
        )

        return MatchModel(data), AwaitingMatch(self._context, data["id"])

    async def create_series(self, match_settings: MatchSeriesSettings,
                            ) -> Tuple[MatchSeriesModel, AwaitingSeries]:
        """Creates a match.

        Parameters
        ----------
        match_settings : MatchSeriesSettings
            Holds details on the match series.

        Returns
        -------
        MatchModel
            Holds match details.
        AwaitingSeries
            Used to interact with a series.
        """

        data = cast(
            dict,
            await self._context._post(
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
            AwaitingSeries(self._context, data["id"])
        )

    async def delete(self) -> None:
        """Used to delete a sever.
        """

        await self._context._delete(
            SERVER.delete.format(self.server_id),
        )

    async def get(self) -> ServerModel:
        """Used to get details on server.

        Returns
        -------
        ServerModel
            Holds data on server.
        """

        return ServerModel(
            cast(
                dict,
                await self._context._get(SERVER.get.format(self.server_id))
            )
        )

    async def update(self, settings: ServerSettings) -> None:
        """Update servers paramters.

        Parameters
        ----------
        settings : ServerSettings
            Used to configure server.
        """

        await self._context._put(
            SERVER.update.format(self.server_id),
            data={
                **settings.payload,
                "server_id": self.server_id
            }
        )

    async def console_send(self, line: str) -> None:
        """Used to send a rcon command to console.

        Parameters
        ----------
        line : str
            Console command.
        """

        await self._context._post(
            url=SERVER.console.format(self.server_id),
            data={
                "line": line,
            }
        )

    async def console_retrive(self, lines: int = 1000) -> list:
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
            await self._context._get(
                url=SERVER.console.format(self.server_id),
                params={
                    "max_lines": lines,
                },
            )
        )

        return data["lines"]

    async def sync(self) -> None:
        """Used to sync files from server to cache.
        """

        await self._context._post(
            url=SERVER.sync.format(self.server_id)
        )

    async def duplicate(self, sync: bool = False,
                        ) -> Tuple[ServerModel, ServerAwaiting]:
        """Used to duplicate a server.

        Parameters
        ----------
        sync : bool
            Used to force update server cache, by default False

        Returns
        -------
        ServerModel
            Holds server data.
        ServerAwaiting
            Used to interact with server.
        """

        if sync:
            await self.sync()

        data = cast(
            dict,
            await self._context._post(
                url=SERVER.duplicate.format(self.server_id),
                read_json=True,
            )
        )

        return ServerModel(data), ServerAwaiting(self._context, data["id"])

    async def ftp_reset(self) -> None:
        """Resets the FRP password.
        """

        await self._context._post(
            url=SERVER.ftp.format(self.server_id)
        )

    async def stop(self) -> None:
        """Used to stop the server.
        """

        await self._context._post(
            url=SERVER.stop.format(self.server_id),
        )

    async def start(self, allow_host_reassignment: bool = True) -> None:
        """Used to start the server.

        Parameters
        ----------
        allow_host_reassignment : bool, optional
            By default True
        """

        await self._context._post(
            url=SERVER.start.format(self.server_id),
            data={"allow_host_reassignment": allow_host_reassignment}
        )

    async def reset(self) -> None:
        """Used to reset the server.
        """

        await self._context._post(
            url=SERVER.reset.format(self.server_id),
        )

    async def files(self, hide_default: bool = False, path: str = None,
                    file_sizes: bool = False,
                    deleted_files: bool = False
                    ) -> AsyncGenerator[Tuple[FileModel, AwaitingFile], None]:
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
        AwaitingFile
            Used to interact with a file.
        """

        data = cast(
            dict,
            await self._context._get(
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

    def file(self, pathway: str) -> AwaitingFile:
        """Used to interact with a file on the server.

        Parameters
        ----------
        pathway : str
            Pathway of file on server.

        Returns
        -------
        AwaitingFile
        """

        return AwaitingFile(
            self._context,
            self.server_id,
            pathway
        )

    async def backups(self
                      ) -> AsyncGenerator[
                          Tuple[BackupModel, AwaitingBackup], None]:
        """Used to list backups a server has.

        Yields
        -------
        BackupModel
            Holds details on backup.
        AwaitingBackup
            Used for interacting with a backup.
        """

        data = cast(
            dict,
            await self._context._get(
                SERVER.backups.format(self.server_id),
            )
        )

        for backup in data:
            yield BackupModel(backup), self.backup(backup["name"])

    def backup(self, backup_name: str) -> AwaitingBackup:
        """Used to interact with a backup.

        Parameters
        ----------
        backup_name : str
            Name of backup.

        Returns
        -------
        AwaitingBackup
        """

        return AwaitingBackup(
            self._context,
            self.server_id,
            backup_name
        )

    async def metrics(self) -> MetricsModel:
        """Used to get server metrics.

        Returns
        -------
        MetricsModel
            Holds details on server metrics.
        """

        data = cast(
            dict,
            await self._context._get(
                SERVER.metrics.format(self.server_id)
            )
        )

        return MetricsModel(data)
