from httpx import Response


class BlockingHttp:
    def __handle_resp(self, resp: Response, json: bool = True) -> None:
        """Handles resp response.

        Parameters
        ----------
        resp
            HTTPX response object.
        """

        resp.raise_for_status()
        return resp.json() if json else True

    def _get(self, *args, **kwargs) -> dict:
        """Wrapped HTTPX Delete.
        """

        with self._client.get(*args, **kwargs) as resp:
            return self.__handle_resp(resp)

    def _delete(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Delete.
        """

        with self._client.delete(*args, **kwargs) as resp:
            return self.__handle_resp(resp, False)

    def _post(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Post.
        """

        with self._client.post(*args, **kwargs) as resp:
            return self.__handle_resp(resp, False)

    def _put(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Put.
        """

        with self._client.put(*args, **kwargs) as resp:
            return self.__handle_resp(resp, False)
