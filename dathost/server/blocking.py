from .base import ServerBase

from ..models.server import ServerModel

from ..settings import ServerSettings

from ..routes import SERVER


class ServerBlocking(ServerBase):
    def delete(self) -> None:
        """Used to delete a sever.
        """

        self.context._delete(
            SERVER.delete.format(self.server_id)
        )

    def get(self) -> ServerModel:
        """Used to get details on server.

        Returns
        -------
        ServerModel
            Holds data on server.
        """

        return ServerModel(
            self.context._get(SERVER.get.format(self.server_id))
        )

    def update(self, settings: ServerSettings) -> None:
        """Update servers paramters.

        Parameters
        ----------
        settings : ServerSettings
            Used to configure server.
        """

        self.context._put(
            SERVER.update.format(self.server_id),
            data={
                **settings.playload,
                "server_id": self.server_id
            }
        )
