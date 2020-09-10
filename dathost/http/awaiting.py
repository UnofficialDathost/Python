from .base import BaseHttp


class AwaitingHttp(BaseHttp):
    async def _get(self, *args, **kwargs) -> dict:
        """Wrapped HTTPX Delete.
        """

        resp = await self._client.get(*args, **kwargs)
        return self.handle_resp(resp)

    async def _delete(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Delete.
        """

        resp = await self._client.delete(*args, **kwargs)
        return self.handle_resp(resp, False)

    async def _post(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Post.
        """

        resp = await self._client.post(*args, **kwargs)
        return self.handle_resp(resp, False)

    async def _put(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Put.
        """

        resp = await self._client.put(*args, **kwargs)
        return self.handle_resp(resp, False)
