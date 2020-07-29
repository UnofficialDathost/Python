import typing

from ..wrapped_requests import AWR
from ..routes import ROUTES

from ..models.server import ServerModel, BackupModel
from ..models.metrics import MetricsModel

from .backup import Backup
from .console import Console
from .file import File


class Server:
    def __init__(self, server_id: str) -> None:
        """
        Used for interacting with a server.

        Parameter
        ---------
        server_id: str
            ID of server.
        """

        self.server_id = server_id

    @property
    def console(self) -> Console:
        """
        Console interactions.

        Returns
        -------
        Console
            Used for interacting with a server's consoles.
        """

        return Console(self.server_id)

    def file(self, pathway: str) -> File:
        """
        Interact with files.

        pathway: str
            Pathway of file on dathost.

        Returns
        -------
        File
            Used for interacting with a servers file.

        Notes
        -----
        The path is counted from the root node as seen in
        the file manager in the control panel,
        i.e. to write csgo/cfg/server.cfg the path would be cfg/server.cfg,
        if the path ends with / a directory will be
        created and the file parameter will be ignored.
        """

        return File(self.server_id, pathway)

    def backup(self, backup_name: str) -> Backup:
        """
        Backup interactions.

        Paramters
        ---------
        backup_name: str
            Name of backup.
        
        Returns
        -------
        Backup
            Used for interacting with a backup.
        """

        return Backup(self.server_id, backup_name)

    async def reset(self) -> bool:
        """
        Resets given server to default files.
        """

        return await AWR(
            ROUTES.server_restart.format(
                self.server_id,
            )
        ).post()

    async def metrics(self) -> MetricsModel:
        """
        Gets metrics about server.

        Returns
        -------
        MetricsModel
            Holds metrics.
        """

        data = await AWR(
            ROUTES.server_metrics.format(
                self.server_id
            )
        ).get()

        return MetricsModel(data)

    async def ftp_reset(self) -> bool:
        """
        Sets a new random FTP password for the server.
        """

        return await AWR(
            ROUTES.ftp_password_reset.format(
                self.server_id
            )
        ).post()

    async def start(self, allow_host_reassignment: bool = True) -> bool:
        """
        Attempts to start given server.

        allow_host_reassignment: bool
            If true, the server may be moved to another host/port
            if the current host is unreachable.
        """

        return await AWR(
            ROUTES.server_start.format(
                self.server_id
            ),
            data={
                "allow_host_reassignment": allow_host_reassignment,
            }
        ).post()

    async def stop(self) -> bool:
        """
        Attempts to stop given server.
        """

        return await AWR(
            ROUTES.server_stop.format(
                self.server_id
            )
        ).post()

    async def sync(self) -> bool:
        """
        Ensures all files are synced.
        """

        return await AWR(
            ROUTES.file_sync.format(
                self.server_id
            )
        ).post()

    async def files(self, pathway: str = None,
                    hide_default_files: bool = False,
                    with_filesizes: bool = False
                    ) -> typing.AsyncGenerator[typing.Any, None]:
        """
        Lists files on the server.

        Paramters
        ---------
        pathway: str
            Path to use as root, leave empty to get all files

        hide_default_files: bool
            If true, only files added by the user will be shown,
            default is all files.

        with_filesizes: bool
            If true, return filesizes with filenames.

        Yields
        ------
        str
            Path to file.
        File
            Used for interacting with a file.
        """

        data = await AWR(
            ROUTES.file_list.format(
                self.server_id
            ),
            params={
                "pathway": pathway,
                "hide_default_files": hide_default_files,
                "with_filesizes": with_filesizes,
            }
        ).get()

        for file in data:
            yield file["path"], File(self.server_id, file["path"])

    async def backups(self) -> typing.AsyncGenerator[typing.Any, None]:
        """
        Lists backups.

        Yields
        ------
        BackupModel
            Holds data around backup.
        Backup
            Used for interacting with a backup.
        """

        data = await AWR(
            ROUTES.server_backup.format(
                self.server_id
            )
        ).get()

        for backup in data:
            yield BackupModel(backup), Backup(self.server_id, backup["name"])

    async def duplicate(self) -> typing.Any:
        """
        Duplicates given server.

        Returns
        -------
        ServerModel
            Holds data on server.
        Server
            Used for interacting with server.
        """

        data = await AWR(
            ROUTES.server_duplicate.format(
                self.server_id
            )
        ).post(json=True)

        return ServerModel(data), Server(data["id"])

    async def delete(self) -> bool:
        """
        Deletes current server.
        """

        return await AWR(
            ROUTES.server_delete.format(
                self.server_id
            )
        ).delete()

    async def get(self) -> ServerModel:
        """
        Gets details about the game server.

        Returns
        -------
        ServerModel
            Holds server data.
        """

        data = await AWR(
            ROUTES.server_get.format(
                self.server_id
            )
        ).get()

        return ServerModel(data)
