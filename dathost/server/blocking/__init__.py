import typing

from ..base import ServerBase

from ...models.server import ServerModel
from ...models.file import FileModel
from ...models.backup import BackupModel

from .backup import Backup

from ...settings import ServerSettings

from ...exceptions import InvalidConsoleLine

from ...routes import SERVER


class ServerBlocking(ServerBase):
    def delete(self) -> None:
        """Used to delete a sever.
        """

        self.context._delete(
            SERVER.delete.format(self.server_id)
        )

    def get(self) -> ServerModel:
        """Used to get details on server.

        Returns
        -------
        ServerModel
            Holds data on server.
        """

        return ServerModel(
            self.context._get(SERVER.get.format(self.server_id))
        )

    def update(self, settings: ServerSettings) -> None:
        """Update servers paramters.

        Parameters
        ----------
        settings : ServerSettings
            Used to configure server.
        """

        self.context._put(
            SERVER.update.format(self.server_id),
            data={
                **settings.playload,
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

        self.context._post(
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

        data = self.context._get(
            url=SERVER.console.format(self.server_id),
            params={
                "max_lines": lines,
            },
        )

        return data["lines"]

    def sync(self) -> None:
        """Used to sync files from server to cache.
        """

        self.context._post(
            url=SERVER.sync.format(self.server_id)
        )

    def duplicate(self, sync: bool = False) -> (ServerModel, ServerBase):
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

        data = self.context._post(
            url=SERVER.duplicate.format(self.server_id),
            read_json=True
        )

        return ServerModel(data), ServerBlocking(self.context, data["id"])

    def ftp_reset(self) -> None:
        """Resets the FRP password.
        """

        self.context._post(
            url=SERVER.ftp.format(self.server_id)
        )

    def stop(self, timeout: int = 60) -> None:
        """Used to stop the server.

        Parameters
        ----------
        timeout : int, optional
            by default 60
        """

        self.context._post(
            url=SERVER.stop.format(self.server_id),
            timeout=timeout
        )

    def start(self, timeout: int = 60) -> None:
        """Used to stop the server.

        Parameters
        ----------
        timeout : int, optional
            by default 60
        """

        self.context._post(
            url=SERVER.start.format(self.server_id),
            timeout=timeout
        )

    def reset(self, timeout: int = 60) -> None:
        """Used to restart the server.

        Parameters
        ----------
        timeout : int, optional
            by default 60
        """

        self.context._post(
            url=SERVER.reset.format(self.server_id),
            timeout=timeout
        )

    def files(self, hide_default: bool = False, path: str = None,
              file_sizes: bool = False, timeout: int = 30
              ) -> typing.AsyncGenerator[FileModel, None]:
        """Used to list files.

        Parameters
        ----------
        hide_default : bool, optional
            by default False
        path : str, optional
            Path to use as root, by default None
        file_sizes : bool, optional
            by default False
        timeout : int
            by default 30

        Yields
        ------
        FileModel
            Holds details on a file.
        """

        data = self.context._get(
            SERVER.files.format(self.server_id),
            params={
                "hide_default_files": hide_default,
                "path": path,
                "with_filesizes": file_sizes,
            },
            timeout=timeout
        )

        for file_ in data:
            yield FileModel(file_)

    def backups(self, timeout: int = 30
                ) -> typing.AsyncGenerator[BackupModel, Backup]:
        """Used to list backups a server has.

        Parameters
        ----------
        timeout : int, optional
            by default 30

        Yields
        -------
        BackupModel
            Holds details on backup.
        Backup
            Used for interacting with a backup.
        """

        data = self.context._get(
            SERVER.backups.format(self.server_id),
            timeout=timeout
        )

        for backup in data:
            yield BackupModel(backup), Backup(
                self.server_id,
                self.context,
                backup["name"]
            )
