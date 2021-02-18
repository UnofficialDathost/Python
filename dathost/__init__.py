import typing

from .base import Base
from .routes import ACCOUNT, CUSTOM_DOMAINS, SERVER

from .http import AwaitingHttp, BlockingHttp

from .server.blocking import ServerBlocking
from .server.awaiting import ServerAwaiting

from .match.awaiting import AwaitingMatch
from .match.blocking import BlockingMatch

from .settings import ServerSettings

from .models.account import AccountModel
from .models.server import ServerModel

from httpx import AsyncClient, Client


__version__ = "0.1.10"
__url__ = "https://dathost.readthedocs.io/en/latest/"
__description__ = "Asynchronous / Synchronous dathost API wrapper."
__author__ = "WardPearce"
__author_email__ = "wardpearce@protonmail.com"
__license__ = "GPL v3"


class Awaiting(Base, AwaitingHttp):
    __client_closed = False

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__create_client()

    async def __aenter__(self) -> None:
        if self.__client_closed:
            self.__create_client()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    def __create_client(self) -> None:
        self._client = AsyncClient(
            auth=self._basic_auth,
            timeout=self._timeout
        )

    async def close(self) -> None:
        """Closes sessions
        """

        self.__client_closed = True
        await self._client.aclose()

    def match(self, match_id: str) -> AwaitingMatch:
        """Used to interact with a match.

        Parameters
        ----------
        match_id : str
            Dathost Match ID.

        Returns
        -------
        AwaitingMatch
        """

        return AwaitingMatch(
            self,
            match_id
        )

    async def create_server(self, settings: ServerSettings
                            ) -> typing.Tuple[ServerModel, ServerAwaiting]:
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
        """

        data = await self._post(
            url=SERVER.create,
            read_json=True,
            data=settings.payload,
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
    __client_closed = False

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__create_client()

    def __enter__(self) -> None:
        if self.__client_closed:
            self.__create_client()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    def close(self) -> None:
        """Closes sessions
        """

        self.__client_closed = True
        self._client.close()

    def __create_client(self) -> None:
        self._client = Client(
            auth=self._basic_auth,
            timeout=self._timeout
        )

    def match(self, match_id: str) -> BlockingMatch:
        """Used to interact with a match.

        Parameters
        ----------
        match_id : str
            Dathost Match ID.

        Returns
        -------
        BlockingMatch
        """

        return BlockingMatch(
            self,
            match_id
        )

    def create_server(self, settings: ServerSettings
                      ) -> typing.Tuple[ServerModel, ServerBlocking]:
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
        """

        data = self._post(
            url=SERVER.create,
            read_json=True,
            data=settings.payload,
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
