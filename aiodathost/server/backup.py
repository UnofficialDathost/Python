from ..wrapped_requests import AWR
from ..routes import ROUTES


class Backup:
    def __init__(self, server_id, backup_name):
        self.server_id = server_id
        self.backup_name = backup_name

    async def restore(self):
        """
        Restores backup to that server.
        """

        return await AWR(
            ROUTES.server_backup_restore.format(
                self.server_id,
                self.backup_name
            )
        ).post()
