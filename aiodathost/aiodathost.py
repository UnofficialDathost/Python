import aiohttp
import asyncio

class dathost:
    """
    Asynchronous wrapper for Dathost's API created by DistrictNine.Host.

    GITHUB: https://github.com/DistrictNineHost/aiodathost

    WEBSITE: https://districtnine.host/

    EMAIL: contact@districtnine.host

    DATHOST:

    WEBSITE: https://dathost.net

    API DOCS: https://dathost.net/api
    """

    def __init__(self, username, password, route = 'https://dathost.net/api/0.1'):
        """ Creates connection session with Dathost.
                - username, REQUIRED - YES | Dathost account username/email.
                - password, REQUIRED - YES | Dathost account password.
                - route,    REQUIRED - NO  | API Route used for all the functions aside from upload.
        """

        self.username = username
        self.password = password
        self.route = route

    def get_auth(self):
        return aiohttp.BasicAuth(login=self.username, password=self.password)

    def aiohttp_init(self, session):
        self.aiohttp_session = session

        return session

    async def _get(self, url, params = {}):
        async with self.aiohttp_session.get(url, params=params) as r:
            if r.status == 200:
                return_data = await r.json()
            else:
                return_data = False

        return return_data

    async def _post(self, url, data = None, params = {}):
        async with self.aiohttp_session.post(url, data=data, params=params) as r:
            return_data = r.status == 200

        return return_data

    async def _delete(self, url,  params = {}):
        async with self.aiohttp_session.delete(url, params=params) as r:
            return_data = r.status == 200

        return return_data

    async def start(self, server_id):
        """ Attempts to start the given server_id.
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
        """

        data = await self._post(url='{}/game-servers/{}/start'.format(self.route, server_id))

        return data

    async def reset(self, server_id):
        """ Attempts to reset the given server_id. (WARNING: THIS COMPLETELY RESETS THE GAME SERVER TO ITS DEFAULT FILES!)
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
        """

        data = await self._post(url='{}/game-servers/{}/reset'.format(self.route, server_id))

        return data

    async def create(self, server_details):
        """ Attempts to spawn a new server with the given parameters.
                - server_details, REQUIRED - YES | Expects a dictionary using these parameters.
                                https://dathost.net/api#!/default/post_game_servers
        """

        data = await self._post(url='{}/game-servers'.format(self.route), params=server_details)

        return data

    async def stop(self, server_id):
        """ Attempts to stop the given server_id.
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
        """

        data = await self._post(url='{}/game-servers/{}/stop'.format(self.route, server_id))

        return data

    async def send_console(self, server_id, console_line):
        """ Attempts to send a single line of text to the console for the given server_id.
                - server_id, REQUIRED - YES    | Dathost's ID used to uniquely identify a game server. 
                - console_line, REQUIRED - YES | Single line of text to send to the console.
        """

        params = {'line': console_line}

        data = await self._post(url='{}/game-servers/{}/console'.format(self.route, server_id), params=params)

        return data

    async def delete(self, server_id):
        """ Attempts to delete the given server_id. (WARNING: ALL FILES & USED CREDIT WILL BE LOST!)
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
        """

        data = self._delete('{}/game-servers/{}'.format(self.route, server_id))

        return  data

    async def delete_file(self, server_id, pathway, file_name):
        """ Attempts to delete a file from the given server_id. (WARNING: THE DELETE FILE WILL BE DELETED!)
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server.
                - pathway,   REQUIRED - YES | The path is counted from the root node as seen in the file manager in the control panel.
                - file_name, REQUIRED - YES | Name of file to delete.
        """

        data = await self._delete(url='{}/game-servers/{}/files/{}{}'.format(self.route, server_id, pathway, file_name))

        return data

    async def sync(self, server_id):
        """ Attempts to sync files for the given server_id.
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
        """

        data = await self._delete(url='{}/game-servers/{}/sync-files'.format(self.route, server_id))

        return data

    async def upload(self, server_id, pathway, local_pathway, file_name, upload_route = 'https://upload.dathost.net/api/0.1'):
        """ Attempts to upload a file to the given server_id. (WARNING: ALL FILES & USED CREDIT WILL BE LOST!)
                - server_id,     REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
                - pathway,       REQUIRED - YES | Pathway to upload to.
                - local_pathway, REQUIRED - YES | Local pathway to pull the file from.
                - file_name,     REQUIRED - YES | Name of file to upload.
                - upload_route,  REQUIRED - NO  | API Route for upload api.
        """

        files = {'file': open(local_pathway, 'rb')}

        # Defaults upload.dathost.host for 500mb max uploads instead of 100mb.
        # Uses upload_route instead of self.route.
        data = await self._post(url='{}/game-servers/{}/files/{}{}'.format(upload_route, server_id, pathway, file_name), data=files)

        return data

    async def unzip(self, server_id, pathway, file_name):
        """ Attempts to upzip a file on the given server_id.
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
                - pathway,   REQUIRED - YES | The path is counted from the root node as seen in the file manager in the control panel.
                - file_name, REQUIRED - YES | Name of file to unzip.
        """

        data = await self._post(url='{}/game-servers/{}/unzip/{}{}'.format(self.route, server_id, pathway, file_name))

        return data

    async def ftp_regenerate(self, server_id):
        """ Attempts to generate a new FTP password for the given server_id.
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
        """

        data = await self._post(url='{}/game-servers/{}/regenerate-ftp-password'.format(self.route, server_id))

        return data

    async def game_details(self, server_id):
        """ Attempts to pull server details from the given server_id.
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
        """

        data = await self._get(url='{}/game-servers/{}'.format(self.route, server_id))

        return data

    async def domains(self):
        """ 
        Attempts to pull Dathost's domains.
        """

        data = await self._get(url='{}/custom-domains'.format(self.route))

        return data

    async def files(self, server_id, pathway = "", hide_default_files = False, with_filesizes = False):
        """ Attempts to list files from the given server_id.
                - server_id,          REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
                - pathway,            REQUIRED - YES | The path is counted from the root node as seen in the file manager in the control panel.
                - hide_default_files, REQUIRED - NO  | Won't return default files if true.
                - with_filesizes,     REQUIRED - NO  | Will return filesizes if true.
        """

        params = {'hide_default_files': str(hide_default_files).lower(), 'path': pathway, 'with_filesizes': str(with_filesizes).lower()}

        data = await self._get(url='{}/game-servers/{}/files'.format(self.route, server_id), params=params)

        return data

    async def download(self, server_id, pathway, file_name):
        """ Attempts to download a file from the given server_id.
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
        """

        data = await self._get(url='{}/game-servers/{}/files/{}{}'.format(self.route, server_id, pathway, file_name))

        return data

    async def get_console(self, server_id, max_lines = 1):
        """ Attempts to pull X amount of lines from the console for the given server_id.
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
                - max_lines, REQUIRED - NO  | Default 1.
        """

        params = {'max_lines': max_lines}

        data = await self._get(url='{}/game-servers/{}/console'.format(self.route, server_id), params=params)

        return data

    async def account(self):
        """
        Returns account infomation.
        """

        data = await self._get(url='{}/account'.format(self.route))

        return data

    async def details(self):
        """
        Returns full list of details about all the game servers currently not deleted in this account.
        """

        data = await self._get(url='{}/game-servers'.format(self.route))

        return data

    async def metrics(self, server_id):
        """ Attempts to pull metrics for the given server_id.
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
        """

        data = await self._get(url='{}/game-servers/{}/metrics'.format(self.route, server_id))

        return data

    async def clone(self, server_id):
        """ Attempts to clone the given server_id.
                - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
        """

        data = await self._post(url='{}/game-servers/{}/duplicate'.format(self.route, server_id))

        return data

# Testing
if __name__ == "__main__":
    dathost = dathost(username="************", password="***********")

    async def testing():
        aiohttp_sess = dathost.aiohttp_init(session=aiohttp.ClientSession(loop=loop, auth=dathost.get_auth()))

        print(await dathost.files(server_id="5ce7d16bff716a453a943807", with_filesizes=True))
        print(await dathost.details())
        print(await dathost.account())

        await aiohttp_sess.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(testing())
    loop.close()