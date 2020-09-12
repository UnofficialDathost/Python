import typing

from .base import Base
from .routes import ACCOUNT, CUSTOM_DOMAINS, SERVER

from .http import AwaitingHttp, BlockingHttp

from .server.blocking import ServerBlocking
from .server.awaiting import ServerAwaiting

from .settings import ServerSettings

from .models.account import AccountModel
from .models.server import ServerModel

from httpx import AsyncClient, Client


__version__ = "0.0.1"
__url__ = "https://github.com/WardPearce/dathost"
__description__ = "Asynchronous / Synchronous dathost API wrapper."
__author__ = "WardPearce"
__author_email__ = "wardpearce@protonmail.com"
__license__ = "GPL v3"


class Awaiting(Base, AwaitingHttp):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._client = AsyncClient(auth=self._basic_auth)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def create_server(self, settings: ServerSettings
                            ) -> (ServerModel, ServerAwaiting):
        """Creates a new server.

        Parameters
        ----------
        settings : ServerSettings
            Used to configure server.

        Returns
        -------
        ServerModel
            Holds data on server.
        ServerAwaiting
            Used to interact with the created server.

        Reference
        ---------
        https://dathost.net/api#/default/post_game_servers

        Notes
        -----
        Any dots (.) should be replaced with double underscore '__'.
        """

        data = await self._post(
            url=SERVER.create,
            read_json=True,
            data=settings.playload,
        )

        return ServerModel(data), self.server(data["id"])

    def server(self, server_id: str) -> ServerAwaiting:
        """Used for interacting with a server.

        Parameters
        ----------
        server_id : str
            Datahost server ID.

        Returns
        -------
        ServerAwaiting
            Used to interact with the server.
        """

        return ServerAwaiting(self, server_id)

    async def servers(self) -> typing.AsyncGenerator[
            ServerModel, ServerAwaiting]:
        """Used to list servers.

        Yields
        -------
        ServerModel
            Holds data on server.
        """

        for server in await self._get(SERVER.list):
            yield ServerModel(server), self.server(server["id"])

    async def close(self) -> None:
        """Closes sessions
        """

        await self._client.aclose()

    async def account(self) -> AccountModel:
        """Gets account details

        Returns
        -------
        AccountModel
            Holds data on a account.
        """

        return AccountModel(
            await self._get(ACCOUNT.details)
        )

    async def domains(self) -> typing.AsyncGenerator[str, None]:
        """Used to list domains.

        Returns
        -------
        list
            List of domains.
        """

        data = await self._get(CUSTOM_DOMAINS.details)
        for domain in data:
            yield domain["name"]


class Blocking(Base, BlockingHttp):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._client = Client(auth=self._basic_auth)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def create_server(self, settings: ServerSettings
                      ) -> (ServerModel, ServerBlocking):
        """Creates a new server.

        Parameters
        ----------
        settings: ServerSettings
            Used to configure server.

        Returns
        -------
        ServerModel
            Holds data on server.
        ServerBlocking
            Used to interact with the created server.

        Reference
        ---------
        https://dathost.net/api#/default/post_game_servers

        Notes
        -----
        Any dots (.) should be replaced with double underscore '__'.
        """

        data = self._post(
            url=SERVER.create,
            read_json=True,
            data=settings.playload,
        )

        return ServerModel(data), self.server(data["id"])

    def server(self, server_id: str) -> ServerBlocking:
        """Used for interacting with a server.

        Parameters
        ----------
        server_id : str
            Datahost server ID.

        Returns
        -------
        ServerBlocking
            Used to interact with the server.
        """

        return ServerBlocking(self, server_id)

    def servers(self) -> typing.Generator[ServerModel, ServerBlocking, None]:
        """Used to list servers.

        Yields
        -------
        ServerModel
            Holds data on server.
        """

        for server in self._get(SERVER.list):
            yield ServerModel(server), self.server(server["id"])

    def close(self) -> None:
        """Closes sessions
        """

        self._client.close()

    def account(self) -> AccountModel:
        """Gets account details

        Returns
        -------
        AccountModel
            Holds data on a account.
        """

        return AccountModel(
            self._get(ACCOUNT.details)
        )

    def domains(self) -> typing.Generator[str, None, None]:
        """Used to list domains.

        Returns
        -------
        list
            List of domains.
        """

        data = self._get(CUSTOM_DOMAINS.details)
        for domain in data:
            yield domain["name"]
