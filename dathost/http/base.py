import typing

from httpx import Response

from ..exceptions import (
    NotFound,
    BadRequest,
    ExceededStorage,
    ServerStart
)


class BaseHttp:
    def handle_resp(self, resp: Response, json: bool = True,
                    read: bool = True) -> typing.Any:
        """Handles resp response.

        Parameters
        ----------
        resp : Response
        json : bool, optional
            by default True
        read : bool, optional
            by default True
        """

        if resp.status_code == 404:
            raise NotFound()
        elif resp.status_code == 400:
            raise BadRequest()
        elif resp.status_code == 507:
            raise ExceededStorage()
        elif resp.status_code == 500:
            raise ServerStart()
        elif resp.status_code != 200:
            resp.raise_for_status()

        if json:
            return resp.json()
        elif read:
            return resp.read()
        else:
            return True
