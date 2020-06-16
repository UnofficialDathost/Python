import aiohttp

from .resources import SESSIONS
from .routes import ROUTES
from .wrapped_requests import AWR

from .models.server import ServerModel
from .models.account import AccountModel

from .server import Server


__version__ = "5.0.0"


class client:
    def __init__(self, email, password, session: aiohttp.ClientSession = None):
        """ Dathost API Interface.
            Parameters
            ----------
            email: str
                Dathost email address.
            password: str
                Dathost password.
            session: aiohttp.ClientSession
                Optionally pass a aiohttp ClientSession.
        """

        SESSIONS.AUTH = aiohttp.BasicAuth(
            email,
            password
        )

        if session:
            SESSIONS.AIOHTTP = session
        else:
            SESSIONS.AIOHTTP = aiohttp.ClientSession()

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

        return await AWR(
            ROUTES.domains
        ).get()

    async def servers(self):
        """
        Lists all non-deleted servers.
        """

        data = await AWR(
            ROUTES.server_list
        ).get()

        for server in data:
            yield ServerModel(server), Server(server["id"])
