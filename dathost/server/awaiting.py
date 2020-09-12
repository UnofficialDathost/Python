from .base import ServerBase

from ..models.server import ServerModel

from ..settings import ServerSettings

from ..exceptions import InvalidConsoleLine

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

    async def console_send(self, line: str) -> None:
        """Used to send a rcon command to console.

        Parameters
        ----------
        line : str
            Console command.
        """

        await self.context._post(
            url=SERVER.console.format(self.server_id),
            data={
                "line": line,
            }
        )

    async def console_retrive(self, lines: int = 1000) -> list:
        """Used to retrive lines from the console.

        Parameters
        ----------
        lines : int, optional
            Amount of lines to retrive, by default 1000

        Returns
        -------
        list
            List of strings.

        Raises
        ------
        InvalidConsoleLine
            Raised when console lines below 1 or above 100000.
        """
        if lines < 1 or lines > 100000:
            raise InvalidConsoleLine()

        data = await self.context._get(
            url=SERVER.console.format(self.server_id),
            params={
                "max_lines": lines,
            },
        )

        return data["lines"]

    async def sync(self) -> None:
        """Used to sync files from server to cache.
        """

        await self.context._post(
            url=SERVER.sync.format(self.server_id)
        )

    async def duplicate(self, sync: bool = False) -> (ServerModel, ServerBase):
        """Used to duplicate a server.

        Parameters
        ----------
        sync : bool
            Used to force update server cache, by default False

        Returns
        -------
        ServerModel
            Holds server data.
        ServerAwaiting
            Used to interact with server.
        """

        if sync:
            await self.sync()

        data = await self.context._post(
            url=SERVER.duplicate.format(self.server_id),
            read_json=True
        )

        return ServerModel(data), ServerAwaiting(self.context, data["id"])

    async def ftp_reset(self) -> None:
        """Resets the FRP password.
        """

        await self.context._post(
            url=SERVER.ftp.format(self.server_id)
        )

    async def stop(self, timeout: int = 60) -> None:
        """Used to stop the server.

        Parameters
        ----------
        timeout : int, optional
            by default 60
        """

        await self.context._post(
            url=SERVER.stop.format(self.server_id),
            timeout=timeout
        )

    async def start(self, timeout: int = 60) -> None:
        """Used to start the server.

        Parameters
        ----------
        timeout : int, optional
            by default 60
        """

        await self.context._post(
            url=SERVER.start.format(self.server_id),
            timeout=timeout
        )

    async def reset(self, timeout: int = 60) -> None:
        """Used to restart the server.

        Parameters
        ----------
        timeout : int, optional
            by default 60
        """

        await self.context._post(
            url=SERVER.reset.format(self.server_id),
            timeout=timeout
        )
