from ..wrapped_requests import AWR
from ..routes import ROUTES

from ..models.server import ServerModel

from .backup import Backup
from .console import Console


class Server:
    def __init__(self, server_id):
        self.server_id = server_id

    @property
    def console(self):
        """
        Console interactions.
        """

        return Console(self.server_id)

    def backup(self, backup_name):
        """
        Backup interactions.
        """

        return Backup(self.server_id, backup_name)

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
