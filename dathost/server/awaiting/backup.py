from ..base import BackupBase

from ...routes import SERVER


class AwaitingBackup(BackupBase):
    async def restore(self) -> None:
        """Used to restore a backup.
        """

        await self.context._post(
            url=SERVER.backup_restore.format(self.server_id, self.backup_name),
        )
