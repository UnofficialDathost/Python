import aiohttp

from .resources import SESSIONS


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
        pass

    async def domains(self):
        pass

    async def servers(self):
        pass
