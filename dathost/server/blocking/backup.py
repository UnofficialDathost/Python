from ..backup_base import BackupBase

from ...routes import SERVER


class BlockingBackup(BackupBase):
    def restore(self, timeout: int = 60) -> None:
        """Used to restore a backup.

        Parameters
        ----------
        timeout : int, optional
            by default 60
        """

        self.context._post(
            url=SERVER.backup_restore.format(self.server_id, self.backup_name),
            timeout=timeout
        )
