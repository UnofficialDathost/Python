from .resources import SESSIONS, CONFIG
from .exceptions import InvalidAuthorization, UndefinedError, \
    BadRequest, RequestTimeout, InternalError, NotFound, AboveDiskQuota


class AWR:
    def __init__(self, route, **kwargs):
        self.route = route

        self.kwargs = kwargs

    def _raise_exception(self, resp):
        if resp.status == 401:
            raise InvalidAuthorization()
        elif resp.status == 404:
            raise NotFound()
        elif resp.status == 400:
            raise BadRequest()
        elif resp.status == 408:
            raise RequestTimeout()
        elif resp.status == 500:
            raise InternalError()
        elif resp.status == 507:
            raise AboveDiskQuota()
        else:
            raise UndefinedError()

    async def get(self, read=False):
        """ Wrapped get request """

        async with SESSIONS.AIOHTTP.get(
            self.route,
            auth=SESSIONS.AUTH,
                **self.kwargs) as resp:
            if resp.status == 200:
                if not read:
                    return await resp.json()
                else:
                    return await resp.read()
            else:
                self._raise_exception(resp)

    async def get_stream(self):
        """
        Steam downloads content.
        """

        async with SESSIONS.AIOHTTP.get(
            self.route,
            auth=SESSIONS.AUTH,
                **self.kwargs) as resp:
            if resp.status == 200:
                chunk = True

                while chunk:
                    chunk = await resp.content.read(CONFIG.chunk_size)

                    if chunk:
                        yield chunk
            else:
                self._raise_exception(resp)

    async def post(self, json=False):
        """ Wrapped post request """

        async with SESSIONS.AIOHTTP.post(
            self.route,
            auth=SESSIONS.AUTH,
                **self.kwargs) as resp:
            if resp.status == 200:
                if not json:
                    return True
                else:
                    return await resp.json()
            else:
                self._raise_exception(resp)

    async def delete(self):
        """ Wrapped delete request """

        async with SESSIONS.AIOHTTP.delete(
            self.route,
            auth=SESSIONS.AUTH,
                **self.kwargs) as resp:
            if resp.status == 200:
                return True
            else:
                self._raise_exception(resp)

    async def put(self):
        """ Wrapped put request """

        async with SESSIONS.AIOHTTP.put(
            self.route,
            auth=SESSIONS.AUTH,
                **self.kwargs) as resp:
            if resp.status == 200:
                return True
            else:
                self._raise_exception(resp)
