from httpx import Response


class BaseHttp:
    def handle_resp(self, resp: Response, json: bool = True) -> None:
        """Handles resp response.

        Parameters
        ----------
        resp
            HTTPX response object.
        """

        resp.raise_for_status()
        return resp.json() if json else True
