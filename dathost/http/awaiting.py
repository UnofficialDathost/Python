from typing import AsyncGenerator, Union, cast
from httpx import AsyncClient
from .base import BaseHttp


class AwaitingHttp(BaseHttp):
    _client: "AsyncClient"

    async def _get(self, url, read_bytes: bool = False,
                   read_json: bool = True, *args, **kwargs
                   ) -> Union[dict, bytes, list]:
        """Wrapped HTTPX Delete.
        """

        return cast(
            Union[dict, bytes],
            self.handle_resp(
                await self._client.get(url, *args, **kwargs),
                read=read_bytes,
                json=read_json
            )
        )

    async def _delete(self, url, *args, **kwargs) -> bool:
        """Wrapped HTTPX Delete.
        """

        return cast(
            bool,
            self.handle_resp(
                await self._client.delete(url, *args, **kwargs),
                False
            )
        )

    async def _post(self, url, read_json: bool = False,
                    *args, **kwargs) -> Union[dict, bool]:
        """Wrapped HTTPX Post.
        """

        return cast(
            Union[dict, bool],
            self.handle_resp(
                await self._client.post(url, *args, **kwargs),
                read_json
            )
        )

    async def _put(self, url, *args, **kwargs) -> bool:
        """Wrapped HTTPX Put.
        """

        return cast(
            bool,
            self.handle_resp(
                await self._client.put(url, *args, **kwargs),
                False
            )
        )

    async def _stream(self, url, *args, **kwargs
                      ) -> AsyncGenerator[bytes, None]:
        """Wrapped HTTPX stream GET.

        Yields
        -------
        bytes
        """

        async with self._client.stream(  # type: ignore
                "GET", url, *args, **kwargs) as resp:
            if resp.status_code == 200:
                async for chunk in resp.aiter_bytes():
                    yield chunk
