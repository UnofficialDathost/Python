import aiohttp

from .resources import SESSIONS, CONFIG
from .routes import ROUTES
from .wrapped_requests import AWR

from .models.server import ServerModel
from .models.account import AccountModel

from .server import Server


__version__ = "5.0.0"


class client:
    def __init__(self, email, password,
                 session: aiohttp.ClientSession = None, chunk_size: int = 25):
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
                How many bytes to load into memory at once.
        """

        CONFIG.chunk_size = chunk_size

        SESSIONS.AUTH = aiohttp.BasicAuth(
            email,
            password
        )

        if session:
            SESSIONS.AIOHTTP = session
        else:
            SESSIONS.AIOHTTP = aiohttp.ClientSession()

    def server(self, server_id=None):
        """
        Object for interacting with a server.
        """

        return Server(server_id)

    async def close(self):
        """
        Force closes any sessions left open.
        """

        await SESSIONS.AIOHTTP.close()

    async def account(self):
        """
        Gets details about account.
        """

        data = await AWR(
            ROUTES.account
        ).get()

        return AccountModel(data)

    async def domains(self):
        """
        Lists all domains.
        """

        data = await AWR(
            ROUTES.domains
        ).get()

        for domain in data:
            yield domain["name"]

    async def servers(self):
        """
        Lists all non-deleted servers.
        """

        data = await AWR(
            ROUTES.server_list
        ).get()

        for server in data:
            yield ServerModel(server), Server(server["id"])
