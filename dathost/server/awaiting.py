from .base import ServerBase

from ..models.server import ServerModel

from ..settings import ServerSettings

from ..routes import SERVER


class ServerAwaiting(ServerBase):
    async def delete(self) -> None:
        """Used to delete a sever.
        """

        await self.context._delete(
            SERVER.delete.format(self.server_id)
        )

    async def get(self) -> ServerModel:
        """Used to get details on server.

        Returns
        -------
        ServerModel
            Holds data on server.
        """

        return ServerModel(
            await self.context._get(SERVER.get.format(self.server_id))
        )

    async def update(self, settings: ServerSettings) -> None:
        """Update servers paramters.

        Parameters
        ----------
        settings : ServerSettings
            Used to configure server.
        """

        await self.context._put(
            SERVER.update.format(self.server_id),
            data={
                **settings.playload,
                "server_id": self.server_id
            }
        )
