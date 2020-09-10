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

        self._client = AsyncClient(self._basic_auth)

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

        data = await self._get(CUSTOM_DOMAINS.details)
        if data:
            return list(data.values())


class Blocking(Base, BlockingHttp):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.client = Client(self._basic_auth)

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

        data = self._get(CUSTOM_DOMAINS.details)
        if data:
            return list(data.values())
