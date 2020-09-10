from .base import ServerBase

from ..routes import SERVER


class ServerAwaiting(ServerBase):
    async def delete(self) -> None:
        """Used to delete a sever.
        """

        await self.context._delete(
            SERVER.delete.format(self.server_id)
        )
