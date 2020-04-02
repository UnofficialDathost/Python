from .routes import ROUTES
from .server import Server
from .misc import Misc

import aiohttp
import asyncio

class client(Misc):
    """ Asynchronous wrapper for Dathost's API. """

    route = "https://dathost.net/api/0.1/"

    def __init__(self, username, password, session=None):
        """ Dathost Object.
                - username, account username/email.
                - password, account password.
        """

        if self.route[-1:] != "/":
            self.route += "/"

        self.routes = ROUTES
        
        # Formatting route into strings
        for key, item in self.routes.items():
            if type(item) == dict:
                for key_1, item_1 in item.items():
                    if type(item_1) == dict:
                        for key_2, item_2 in item_1.items():
                            if type(item_2) == dict:
                                for key_3 in item_2.keys():
                                    self.routes[key][key_1][key_2][key_3] = self.route + self.routes[key][key_1][key_2][key_3]
                            else:
                                self.routes[key][key_1][key_2] = self.route + self.routes[key][key_1][key_2]
                    else:
                        self.routes[key][key_1] = self.route + self.routes[key][key_1]
            else:
                self.routes[key] = self.route + self.routes[key]

        self.auth = aiohttp.BasicAuth(login=username, password=password)

        if session:
            self.session = session
        else:
            self.session = aiohttp.ClientSession(loop=asyncio.get_event_loop())

    async def _get(self, return_read=False, **kwargs):
        async with self.session.get(auth=self.auth, **kwargs) as resp:
            if resp.status == 200:
                if return_read:
                    return await resp.read()
                else:
                    return await resp.json()
            else:
                return False
 
    async def _post(self, **kwargs):
        async with self.session.post(auth=self.auth, **kwargs) as resp:
            return resp.status == 200

    async def _delete(self, **kwargs):
        async with self.session.delete(auth=self.auth, **kwargs) as resp:
            return resp.status == 200

    def server(self, server_id=None):
        """ Server object.
                - server_id, not required.
        """

        return Server(server_id=server_id, obj=self)