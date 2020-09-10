from .base import BaseHttp


class BlockingHttp(BaseHttp):
    def _get(self, *args, **kwargs) -> dict:
        """Wrapped HTTPX Delete.
        """

        resp = self._client.get(*args, **kwargs)
        return self.handle_resp(resp)

    def _delete(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Delete.
        """

        resp = self._client.delete(*args, **kwargs)
        return self.handle_resp(resp, False)

    def _post(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Post.
        """

        resp = self._client.post(*args, **kwargs)
        return self.handle_resp(resp, False)

    def _put(self, *args, **kwargs) -> bool:
        """Wrapped HTTPX Put.
        """

        resp = self._client.put(*args, **kwargs)
        return self.handle_resp(resp, False)
