from httpx import Response


class AwaitingHttp:
    async def __handle_resp(self, resp: Response, json: bool = True) -> None:
        """Handles resp response.

        Parameters
        ----------
        resp
            HTTPX response object.
        """

        resp.raise_for_status()
        return await resp.json() if json else True

    async def _get(self, *args, **kwargs) -> dict:
        """Wrapped HTTPX Delete.
        """

        async with self._client.get(*args, **kwargs) as resp:
            return await self.__handle_resp(resp)

    async def _delete(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Delete.
        """

        async with self._client.delete(*args, **kwargs) as resp:
            return await self.__handle_resp(resp, False)

    async def _post(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Post.
        """

        async with self._client.post(*args, **kwargs) as resp:
            return await self.__handle_resp(resp, False)

    async def _put(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Put.
        """

        async with self._client.put(*args, **kwargs) as resp:
            return await self.__handle_resp(resp, False)
