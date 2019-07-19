import aiohttp

class dathost:
    def __init__(self, username, password):
        self.auth = aiohttp.BasicAuth(login=username, password=password)

    async def start(self, server_id):
        """ Starts given server id. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.post('https://dathost.net/api/0.1/game-servers/{}/start'.format(server_id)) as r:
                data = r.status == 200

        session_object.close

        return data

    async def stop(self, server_id):
        """ Stops given server. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.post('https://dathost.net/api/0.1/game-servers/{}/stop'.format(server_id)) as r:
                data = r.status == 200

        session_object.close

        return data

    async def send_console(self, server_id, console_line):
        """ Sends a line to the console. """

        params = {'line': console_line}

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.post('https://dathost.net/api/0.1/game-servers/{}/console'.format(server_id), params=params) as r:
                data = r.status == 200

        session_object.close

        return data

    async def delete(self, server_id):
        """ Deletes given server. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.delete('https://dathost.net/api/0.1/game-servers/{}'.format(server_id)) as r:
                data = r.status == 200

        session_object.close

        return  data

    async def delete_file(self, server_id, pathway, file_name):
        """ Deletes file from given server. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.delete('https://dathost.net/api/0.1/game-servers/{}/files/{}{}'.format(server_id, pathway, file_name)) as r:
                data = r.status == 200

        session_object.close

        return data

    async def sync(self, server_id):
        """ Syncs files between given server. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.post('https://dathost.net/api/0.1/game-servers/{}/sync-files'.format(server_id)) as r:
                data = r.status == 200

        session_object.close

        return data

    async def ftp_regenerate(self, server_id):
        """ Generate a new random ftp password. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.post('https://dathost.net/api/0.1/game-servers/{}/regenerate-ftp-password'.format(server_id)) as r:
                data = r.status == 200

        session_object.close

        return data

    async def game_details(self, server_id):
        """ Returns details on a game server. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.get('https://dathost.net/api/0.1/game-servers/{}'.format(server_id)) as r:
                if r.status == 200:
                    data = await r.json()
                else:
                    data = False

        session_object.close

        return data

    async def download(self, server_id, pathway, file_name):
        """ Downloads a file from the game server. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.get('https://dathost.net/api/0.1/game-servers/{}/files/{}{}'.format(server_id, pathway, file_name)) as r:
                if r.status == 200:
                    data = await r.read()
                else:
                    data = False

        session_object.close

        return data

    async def account(self):
        """ Returns account infomation. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.get('https://dathost.net/api/0.1/account') as r:
                if r.status == 200:
                    data = await r.json()
                else:
                    data = False

        session_object.close

        return data

    async def details(self):
        """ Returns full list of details about all the game servers. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.get('https://dathost.net/api/0.1/game-servers') as r:
                if r.status == 200:
                    data = await r.json()
                else:
                    data = False

        session_object.close

        return data

    async def metrics(self, server_id):
        """ Returns metricis saved by dathost about a game server. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.get('https://dathost.net/api/0.1/game-servers/{}/metrics'.format(server_id)) as r:
                if r.status == 200:
                    data = await r.json()
                else:
                    data = False

        session_object.close

        return data

    async def clone(self, server_id):
        """ Clones a game server and returns infomation on it. """

        session_object = aiohttp.ClientSession(auth=self.auth)
        async with session_object as session:
            async with session.post('https://dathost.net/api/0.1/game-servers/{}/duplicate'.format(server_id)) as r:
                if r.status == 200:
                    data = await r.json()
                else:
                    data = False

        session_object.close

        return data
