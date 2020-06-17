from ..wrapped_requests import AWR
from ..routes import ROUTES

from ..models.server import ServerModel

from .backup import Backup
from .console import Console
from .file import File


class Server:
    def __init__(self, server_id):
        self.server_id = server_id

    @property
    def console(self):
        """
        Console interactions.
        """

        return Console(self.server_id)

    def file(self, pathway: str):
        """
        Interact with files.

        pathway: str
            Pathway of file on dathost.
        """

        return File(self.server_id, pathway)

    def backup(self, backup_name):
        """
        Backup interactions.
        """

        return Backup(self.server_id, backup_name)

    async def files(self, pathway: str = None,
                    hide_default_files: bool = False,
                    with_filesizes: bool = False):
        """
        Lists files on the server.

        pathway: str
            Path to use as root, leave empty to get all files

        hide_default_files: bool
            If true, only files added by the user will be shown,
            default is all files.

        with_filesizes: bool
            If true, return filesizes with filenames
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

    async def backups(self):
        """
        Lists backups.
        """

        data = await AWR(
            ROUTES.server_backup.format(
                self.server_id
            )
        )

        # Add model response once i get the schema.
        # Should response with the Backup object too.

        return data

    async def duplicate(self):
        """
        Duplicates given server.
        """

        data = await AWR(
            ROUTES.server_duplicate.format(
                self.server_id
            )
        ).post(json=True)

        return ServerModel(data), Server(data["id"])

    async def delete(self):
        """
        Deletes current server.
        """

        return await AWR(
            ROUTES.server_delete.format(
                self.server_id
            )
        ).delete()

    async def get(self):
        """
        Gets details about the game server.
        """

        data = await AWR(
            ROUTES.server_get.format(
                self.server_id
            )
        )

        return ServerModel(data)
