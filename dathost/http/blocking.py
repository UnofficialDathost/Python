from .base import BaseHttp


class BlockingHttp(BaseHttp):
    def _get(self, url, read_bytes: bool = False,
             read_json: bool = True, *args, **kwargs) -> dict:
        """Wrapped HTTPX Delete.
        """

        return self.handle_resp(
            self._client.get(url, *args, **kwargs),
            json=read_json,
            read=read_bytes
        )

    def _delete(self, url, *args, **kwargs) -> bool:
        """Wrapped HTTPX Delete.
        """

        return self.handle_resp(
            self._client.delete(url, *args, **kwargs),
            False
        )

    def _post(self, url, read_json: bool = False,
              *args, **kwargs) -> bool:
        """Wrapped HTTPX Post.
        """

        return self.handle_resp(
            self._client.post(url, *args, **kwargs),
            read_json
        )

    def _put(self, url, *args, **kwargs) -> bool:
        """Wrapped HTTPX Put.
        """

        return self.handle_resp(
            self._client.put(url, *args, **kwargs),
            False
        )
