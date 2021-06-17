import logging
from typing import Union

from httpx import Response
from json import JSONDecodeError

from ..exceptions import (
    NotFound,
    BadRequest,
    ExceededStorage,
    ServerStart
)


class BaseHttp:
    def handle_resp(self,
                    resp: Response,
                    json: bool = True,
                    read: bool = True
                    ) -> Union[bool, bytes, dict, None]:
        """Handles resp response.

        Parameters
        ----------
        resp : Response
        json : bool, optional
            by default True
        read : bool, optional
            by default True
        """

        if resp.status_code == 200:
            if json:
                return resp.json()
            elif read:
                return resp.read()
            else:
                return True
        else:
            try:
                message = resp.json()
            except JSONDecodeError:
                message = None
            else:
                logging.error(message)

            if resp.status_code == 404:
                raise NotFound(message)
            elif resp.status_code == 400:
                raise BadRequest(message)
            elif resp.status_code == 507:
                raise ExceededStorage(message)
            elif resp.status_code == 500:
                raise ServerStart(message)
            else:
                resp.raise_for_status()
