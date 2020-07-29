import aiohttp
import typing

from .resources import Sessions, Config
from .routes import ROUTES
from .wrapped_requests import AWR

from .models.server import ServerModel
from .models.account import AccountModel

from .server import Server


__version__ = "5.1.0"


class client:
    def __init__(self, email: str, password: str,
                 session: aiohttp.ClientSession = None,
                 chunk_size: int = 25) -> None:
        """ Dathost API Interface.
            Parameters
            ----------
            email: str
                Dathost email address.
            password: str
                Dathost password.
            session: aiohttp.ClientSession
                Optionally pass a aiohttp ClientSession.
            chunk_size: int
                How many bytes to load into memory at once (default 25).
        """

        Config.chunk_size = chunk_size

        Sessions.AUTH = aiohttp.BasicAuth(
            email,
            password
        )

        if session:
            Sessions.AIOHTTP = session
        else:
            Sessions.AIOHTTP = aiohttp.ClientSession()

    async def create_server(self, **kwargs) -> (ServerModel, Server):
        """
        Creates a server, responses with the data & sets the current
        initialized object to the created server's ID.

        Returns
        -------
        ServerModel
            Holds server data.
        Server
            Used for interacting with server.

        Notes
        -----
        If the parameter includes a '.' replace it with '__'.
        """

        params = {}
        for key in kwargs:
            params[key.replace("__", ".")] = kwargs[key]

        data = await AWR(
            ROUTES.server_create,
            params=params
        ).post(json=True)

        return ServerModel(data), Server(data["id"])

    def server(self, server_id: str) -> Server:
        """
        Object for interacting with a server.

        Paramters
        ---------
        server_id: str
            ID of server.
        """

        return Server(server_id)

    async def close(self) -> None:
        """
        Force closes any sessions left open.

        Notes
        -----
        This should always be ran at program shutdown.
        """

        await Sessions.AIOHTTP.close()

    async def account(self) -> AccountModel:
        """
        Gets details about account.
        """

        data = await AWR(
            ROUTES.account
        ).get()

        return AccountModel(data)

    async def domains(self) -> typing.AsyncGenerator[typing.Any, None]:
        """
        Lists all domains.

        Yields
        ------
        str
            Domain string.
        """

        data = await AWR(
            ROUTES.domains
        ).get()

        for domain in data:
            yield domain["name"]

    async def servers(self) -> typing.AsyncGenerator[typing.Any, None]:
        """
        Lists all non-deleted servers.

        Yields
        ------
        ServerModel
            Holds server data.
        Server
            Used for interacting with the server.
        """

        data = await AWR(
            ROUTES.server_list
        ).get()

        for server in data:
            yield ServerModel(server), Server(server["id"])
