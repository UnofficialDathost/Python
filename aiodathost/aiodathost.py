import aiohttp
import asyncio

class dathost:
    def __init__(self, username, password, route = 'https://dathost.net/api/0.1'):
        auth = aiohttp.BasicAuth(login=username, password=password)
        self.session = aiohttp.ClientSession(auth=auth)
        self.route = route

    async def start(self, server_id):
        """ Starts given server id. """

        async with self.session.post('{}/game-servers/{}/start'.format(self.route, server_id)) as r:
            data = r.status == 200

        return data

    async def reset(self, server_id):
        """ Resets given server id. """

        async with self.session.post('{}/game-servers/{}/reset'.format(self.route, server_id)) as r:
            data = r.status == 200

        return data

    async def create(self, server_details):
        """ 
        Spawns new dathost server. 
        https://dathost.net/api#!/default/post_game_servers
        """

        async with self.session.post('{}/game-servers'.format(self.route), params=server_details) as r:
            data = r.status == 200

        return data

    async def stop(self, server_id):
        """ Stops given server. """

        async with self.session.post('{}/game-servers/{}/stop'.format(self.route, server_id)) as r:
            data = r.status == 200

        return data

    async def send_console(self, server_id, console_line):
        """ Sends a line to the console. """

        params = {'line': console_line}

        async with self.session.post('{}/game-servers/{}/console'.format(self.route, server_id), params=params) as r:
            data = r.status == 200

        return data

    async def delete(self, server_id):
        """ Deletes given server. """

        async with self.session.delete('{}/game-servers/{}'.format(self.route, server_id)) as r:
            data = r.status == 200

        return  data

    async def delete_file(self, server_id, pathway, file_name):
        """ Deletes file from given server. """

        async with self.session.delete('{}/game-servers/{}/files/{}{}'.format(self.route, server_id, pathway, file_name)) as r:
            data = r.status == 200

        return data

    async def sync(self, server_id):
        """ Syncs files between given server. """

        async with self.session.post('{}/game-servers/{}/sync-files'.format(self.route, server_id)) as r:
            data = r.status == 200

        return data

    async def upload(self, server_id, pathway, local_pathway, file_name, upload_route = 'https://upload.dathost.net/api/0.1'):
        """ Uploads file to game server. """

        files = {'file': open(local_pathway, 'rb')}

        # Defaults upload.dathost.host for 500mb max uploads instead of 100mb.
        # Uses upload_route instead of self.route.
        async with self.session.post('{}/game-servers/{}/files/{}{}'.format(upload_route, server_id, pathway, file_name), data=files) as r:
            data = r.status == 200

        return data

    async def unzip(self, server_id, pathway, file_name):
        """ Unzips file on game server. """

        async with self.session.post('{}/game-servers/{}/unzip/{}{}'.format(self.route, server_id, pathway, file_name)) as r:
            data = r.status == 200

        return data

    async def ftp_regenerate(self, server_id):
        """ Generate a new random ftp password. """

        async with self.session.post('{}/game-servers/{}/regenerate-ftp-password'.format(self.route, server_id)) as r:
            data = r.status == 200

        return data

    async def game_details(self, server_id):
        """ Returns details on a game server. """

        async with self.session.get('{}/game-servers/{}'.format(self.route, server_id)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def domains(self):
        """ Returns list of domains on dathost. """

        async with self.session.get('{}/custom-domains'.format(self.route)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def files(self, server_id, path = "", hide_default_files = False, with_filesizes = False):
        """ Returns files on a game server. """

        params = {'hide_default_files': hide_default_files, 'path': path, 'with_filesizes': with_filesizes}

        async with self.session.get('{}/game-servers/{}/files'.format(self.route, server_id), params=params) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def download(self, server_id, pathway, file_name):
        """ Downloads a file from the game server. """

        async with self.session.get('{}/game-servers/{}/files/{}{}'.format(self.route, server_id, pathway, file_name)) as r:
            if r.status == 200:
                data = await r.read()
            else:
                data = False

        return data

    async def get_console(self, server_id, max_lines = 1):
        """ Gets x amount of lines from the console from the game server. """

        params = {'max_lines': max_lines}

        async with self.session.get('{}/game-servers/{}/console'.format(self.route, server_id), params=params) as r:
            if r.status == 200:
                data = await r.read()
            else:
                data = False

        return data

    async def account(self):
        """ Returns account infomation. """

        async with self.session.get('{}/account'.format(self.route)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def details(self):
        """ Returns full list of details about all the game servers. """

        async with self.session.get('{}/game-servers'.format(self.route)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def metrics(self, server_id):
        """ Returns metricis saved by dathost about a game server. """

        async with self.session.get('{}/game-servers/{}/metrics'.format(self.route, server_id)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def clone(self, server_id):
        """ Clones a game server and returns infomation on it. """

        async with self.session.post('{}/game-servers/{}/duplicate'.format(self.route, server_id)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

# Testing
if __name__ == "__main__":
    dathost = dathost(username="*****", password="****")

    async def testing():
        print(await dathost.details())
        print(await dathost.details())

        await dathost.session.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(testing())
    loop.close()