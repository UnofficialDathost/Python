from .resources import SESSIONS
from .exceptions import InvalidAuthorization, UndefinedError, \
    BadRequest, RequestTimeout, InternalError


class AWR:
    def __init__(self, route, **kwargs):
        self.route = route

        self.kwargs = kwargs

    async def _raise_exception(self, resp):
        error_message = await resp.json()

        if "response" in error_message \
                and "error" in error_message["response"]:
            error_message = error_message["response"]["error"]
        else:
            error_message = None

        if resp.status == 401:
            raise InvalidAuthorization(error_message)
        elif resp.status == 400:
            raise BadRequest(error_message)
        elif resp.status == 408:
            raise RequestTimeout(error_message)
        elif resp.status == 500:
            raise InternalError(error_message)
        else:
            raise UndefinedError(error_message)

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
                await self._raise_exception(resp)

    async def post(self):
        """ Wrapped post request """

        async with SESSIONS.AIOHTTP.post(
            self.route,
            auth=SESSIONS.AUTH,
                **self.kwargs) as resp:
            if resp.status == 200:
                return await resp.json()
            else:
                await self._raise_exception(resp)

    async def delete(self):
        """ Wrapped delete request """

        async with SESSIONS.AIOHTTP.delete(
            self.route,
            auth=SESSIONS.AUTH,
                **self.kwargs) as resp:
            if resp.status == 200:
                return await resp.json()
            else:
                await self._raise_exception(resp)

    async def put(self):
        """ Wrapped put request """

        async with SESSIONS.AIOHTTP.put(
            self.route,
            auth=SESSIONS.AUTH,
                **self.kwargs) as resp:
            if resp.status == 200:
                return await resp.json()
            else:
                await self._raise_exception(resp)
