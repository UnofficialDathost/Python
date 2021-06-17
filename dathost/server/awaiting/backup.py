from typing import TYPE_CHECKING

from ..base import BackupBase
from ...routes import SERVER

if TYPE_CHECKING:
    from ... import Awaiting


class AwaitingBackup(BackupBase):
    _context: "Awaiting"

    async def restore(self) -> None:
        """Used to restore a backup.
        """

        await self._context._post(
            url=SERVER.backup_restore.format(self.server_id, self.backup_name),
        )
