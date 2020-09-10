from .base import Base
from .routes import ACCOUNT, CUSTOM_DOMAINS

from .http import AwaitingHttp, BlockingHttp

from .models.account import AccountModel

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

    async def domains(self) -> list:
        """Used to list domains.

        Returns
        -------
        list
            List of domains.
        """

        return await self._get(CUSTOM_DOMAINS.details)


class Blocking(Base, BlockingHttp):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._client = Client(auth=self._basic_auth)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

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

    def domains(self) -> list:
        """Used to list domains.

        Returns
        -------
        list
            List of domains.
        """

        return self._get(CUSTOM_DOMAINS.details)
