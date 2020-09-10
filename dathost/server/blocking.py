from .base import ServerBase

from ..routes import SERVER


class ServerBlocking(ServerBase):
    def delete(self) -> None:
        """Used to delete a sever.
        """

        self.context._delete(
            SERVER.delete.format(self.server_id)
        )
