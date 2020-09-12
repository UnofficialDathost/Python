import typing

from .base import BaseHttp


class AwaitingHttp(BaseHttp):
    async def _get(self, *args, **kwargs) -> dict:
        """Wrapped HTTPX Delete.
        """

        return self.handle_resp(
            await self._client.get(*args, **kwargs)
        )

    async def _delete(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Delete.
        """

        return self.handle_resp(
            await self._client.delete(*args, **kwargs),
            False
        )

    async def _post(self, read_json: bool = False,
                    *args, **kwargs) -> bool:
        """Wrapped HTTPX Post.
        """

        return self.handle_resp(
            await self._client.post(*args, **kwargs),
            read_json
        )

    async def _put(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Put.
        """

        return self.handle_resp(
            await self._client.put(*args, **kwargs),
            False
        )

    async def _stream(self,  *args, **kwargs
                      ) -> typing.AsyncGenerator[bytes, None]:
        """Wrapped HTTPX stream GET.

        Yields
        -------
        bytes
        """

        async with self._client.stream("GET", *args, **kwargs) as resp:
            if resp.status_code == 200:
                async for chunk in resp.aiter_bytes():
                    yield chunk
