import aiohttp
import asyncio

class dathost:
    def __init__(self, username, password):
        self.auth = aiohttp.BasicAuth(login=username, password=password)
        self.session = aiohttp.ClientSession(auth=self.auth)

    async def start(self, server_id):
        """ Starts given server id. """

        async with self.session.post('https://dathost.net/api/0.1/game-servers/{}/start'.format(server_id)) as r:
            data = r.status == 200

        return data

    async def create(self, server_details):
        """ 
        Spawns new dathost server. 
        https://dathost.net/api#!/default/post_game_servers
        """

        async with self.session.post('https://dathost.net/api/0.1/game-servers', params=server_details) as r:
            data = r.status == 200

        return data

    async def stop(self, server_id):
        """ Stops given server. """

        async with self.session.post('https://dathost.net/api/0.1/game-servers/{}/stop'.format(server_id)) as r:
            data = r.status == 200

        return data

    async def send_console(self, server_id, console_line):
        """ Sends a line to the console. """

        params = {'line': console_line}

        async with self.session.post('https://dathost.net/api/0.1/game-servers/{}/console'.format(server_id), params=params) as r:
            data = r.status == 200

        return data

    async def delete(self, server_id):
        """ Deletes given server. """

        async with self.session.delete('https://dathost.net/api/0.1/game-servers/{}'.format(server_id)) as r:
            data = r.status == 200

        return  data

    async def delete_file(self, server_id, pathway, file_name):
        """ Deletes file from given server. """

        async with self.session.delete('https://dathost.net/api/0.1/game-servers/{}/files/{}{}'.format(server_id, pathway, file_name)) as r:
            data = r.status == 200

        return data

    async def sync(self, server_id):
        """ Syncs files between given server. """

        async with self.session.post('https://dathost.net/api/0.1/game-servers/{}/sync-files'.format(server_id)) as r:
            data = r.status == 200

        return data

    async def upload(self, server_id, pathway, local_pathway, file_name):
        """ Uploads file to game server. """

        files = {'file': open(local_pathway, 'rb')}

        async with self.session.post('https://upload.dathost.net/api/0.1/game-servers/{}/files/{}{}'.format(server_id, pathway, file_name), data=files) as r:
            data = r.status == 200

        return data

    async def unzip(self, server_id, pathway, file_name):
        """ Unzips file on game server. """

        async with self.session.post('https://dathost.net/api/0.1/game-servers/{}/unzip/{}{}'.format(server_id, pathway, file_name)) as r:
            data = r.status == 200

        return data

    async def ftp_regenerate(self, server_id):
        """ Generate a new random ftp password. """

        async with self.session.post('https://dathost.net/api/0.1/game-servers/{}/regenerate-ftp-password'.format(server_id)) as r:
            data = r.status == 200

        return data

    async def game_details(self, server_id):
        """ Returns details on a game server. """

        async with self.session.get('https://dathost.net/api/0.1/game-servers/{}'.format(server_id)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def domains(self):
        """ Returns list of domains on dathost. """

        async with self.session.get('https://dathost.net/api/0.1/custom-domains') as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def files(self, server_id, path = "", hide_default_files = False, with_filesizes = False):
        """ Returns files on a game server. """

        params = {'hide_default_files': hide_default_files, 'path': path, 'with_filesizes': with_filesizes}

        async with self.session.get('https://dathost.net/api/0.1/game-servers/{}/files'.format(server_id), params=params) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def download(self, server_id, pathway, file_name):
        """ Downloads a file from the game server. """

        async with self.session.get('https://dathost.net/api/0.1/game-servers/{}/files/{}{}'.format(server_id, pathway, file_name)) as r:
            if r.status == 200:
                data = await r.read()
            else:
                data = False

        return data

    async def get_console(self, server_id, max_lines = 1):
        """ Gets x amount of lines from the console from the game server. """

        params = {'max_lines': max_lines}

        async with self.session.get('https://dathost.net/api/0.1/game-servers/{}/console'.format(server_id), params=params) as r:
            if r.status == 200:
                data = await r.read()
            else:
                data = False

        return data

    async def account(self):
        """ Returns account infomation. """

        async with self.session.get('https://dathost.net/api/0.1/account') as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def details(self):
        """ Returns full list of details about all the game servers. """

        async with self.session.get('https://dathost.net/api/0.1/game-servers') as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def metrics(self, server_id):
        """ Returns metricis saved by dathost about a game server. """

        async with self.session.get('https://dathost.net/api/0.1/game-servers/{}/metrics'.format(server_id)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def clone(self, server_id):
        """ Clones a game server and returns infomation on it. """

        async with self.session.post('https://dathost.net/api/0.1/game-servers/{}/duplicate'.format(server_id)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

if __name__ == "__main__":
    dathost = dathost(username="wpearce6@gmail.com", password="sdABt8zhP8Ah3cv")

    async def testing():
        print(await dathost.details())
        print(await dathost.details())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(testing())
    loop.close()