from .base import BaseHttp


class BlockingHttp(BaseHttp):
    def _get(self, *args, **kwargs) -> dict:
        """Wrapped HTTPX Delete.
        """

        return self.handle_resp(
            self._client.get(*args, **kwargs)
        )

    def _delete(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Delete.
        """

        return self.handle_resp(
            self._client.delete(*args, **kwargs),
            False
        )

    def _post(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Post.
        """

        return self.handle_resp(
            self._client.post(*args, **kwargs),
            False
        )

    def _put(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Put.
        """

        return self.handle_resp(
            self._client.put(*args, **kwargs),
            False
        )
