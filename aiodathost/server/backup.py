from ..wrapped_requests import AWR
from ..routes import ROUTES


class Backup:
    def __init__(self, server_id: str, backup_name: str) -> None:
        """
        Paramters
        ---------
        server_id: str
        backup_name: str
        """

        self.server_id = server_id
        self.backup_name = backup_name

    async def restore(self) -> bool:
        """
        Restores backup to that server.
        """

        return await AWR(
            ROUTES.server_backup_restore.format(
                self.server_id,
                self.backup_name
            )
        ).post()
