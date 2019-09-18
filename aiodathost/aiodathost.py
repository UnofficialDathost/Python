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
        auth = aiohttp.BasicAuth(login=username, password=password)
        self.session = aiohttp.ClientSession(auth=auth)
        self.route = route

    class server:
        """
        Game server interactions.
        """

        async def start(self, server_id):
            """ Attempts to start the given server_id.
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
            """

            async with self.session.post('{}/game-servers/{}/start'.format(self.route, server_id)) as r:
                data = r.status == 200

            return data

        async def reset(self, server_id):
            """ Attempts to reset the given server_id. (WARNING: THIS COMPLETELY RESETS THE GAME SERVER TO ITS DEFAULT FILES!)
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
            """

            async with self.session.post('{}/game-servers/{}/reset'.format(self.route, server_id)) as r:
                data = r.status == 200

            return data

        async def create(self, server_details):
            """ Attempts to spawn a new server with the given parameters.
                    - server_details, REQUIRED - YES | Expects a dictionary using these parameters.
                                    https://dathost.net/api#!/default/post_game_servers
            """

            async with self.session.post('{}/game-servers'.format(self.route), params=server_details) as r:
                data = r.status == 200

            return data

        async def clone(self, server_id):
            """ Attempts to clone the given server_id.
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
            """

            async with self.session.post('{}/game-servers/{}/duplicate'.format(self.route, server_id)) as r:
                if r.status == 200:
                    data = await r.json()
                else:
                    data = False

            return data

        async def stop(self, server_id):
            """ Attempts to stop the given server_id.
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
            """

            async with self.session.post('{}/game-servers/{}/stop'.format(self.route, server_id)) as r:
                data = r.status == 200

            return data

        async def delete(self, server_id):
            """ Attempts to delete the given server_id. (WARNING: ALL FILES & USED CREDIT WILL BE LOST!)
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
            """

            async with self.session.delete('{}/game-servers/{}'.format(self.route, server_id)) as r:
                data = r.status == 200

            return  data

        async def ftp_regenerate(self, server_id):
            """ Attempts to generate a new FTP password for the given server_id.
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
            """

            async with self.session.post('{}/game-servers/{}/regenerate-ftp-password'.format(self.route, server_id)) as r:
                data = r.status == 200

            return data

        async def details(self, server_id):
            """ Attempts to pull server details from the given server_id.
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
            """

            async with self.session.get('{}/game-servers/{}'.format(self.route, server_id)) as r:
                if r.status == 200:
                    data = await r.json()
                else:
                    data = False

            return data

    class files:
        """
        Game server file interactions.
        """

        async def delete(self, server_id, pathway, file_name):
            """ Attempts to delete a file from the given server_id. (WARNING: THE DELETE FILE WILL BE DELETED!)
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server.
                    - pathway,   REQUIRED - YES | The path is counted from the root node as seen in the file manager in the control panel.
                    - file_name, REQUIRED - YES | Name of file to delete.
            """

            async with self.session.delete('{}/game-servers/{}/files/{}{}'.format(self.route, server_id, pathway, file_name)) as r:
                data = r.status == 200

            return data

        async def sync(self, server_id):
            """ Attempts to sync files for the given server_id.
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
            """

            async with self.session.post('{}/game-servers/{}/sync-files'.format(self.route, server_id)) as r:
                data = r.status == 200

            return data

        async def metrics(self, server_id):
            """ Attempts to pull metrics for the given server_id.
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
            """

            async with self.session.get('{}/game-servers/{}/metrics'.format(self.route, server_id)) as r:
                if r.status == 200:
                    data = await r.json()
                else:
                    data = False

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
            async with self.session.post('{}/game-servers/{}/files/{}{}'.format(upload_route, server_id, pathway, file_name), data=files) as r:
                data = r.status == 200

            return data

        async def download(self, server_id, pathway, file_name):
            """ Attempts to download a file from the given server_id.
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
            """

            async with self.session.get('{}/game-servers/{}/files/{}{}'.format(self.route, server_id, pathway, file_name)) as r:
                if r.status == 200:
                    data = await r.read()
                else:
                    data = False

            return data

        async def unzip(self, server_id, pathway, file_name):
            """ Attempts to upzip a file on the given server_id.
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
                    - pathway,   REQUIRED - YES | The path is counted from the root node as seen in the file manager in the control panel.
                    - file_name, REQUIRED - YES | Name of file to unzip.
            """

            async with self.session.post('{}/game-servers/{}/unzip/{}{}'.format(self.route, server_id, pathway, file_name)) as r:
                data = r.status == 200

            return data

        async def list(self, server_id, pathway = "", hide_default_files = False, with_filesizes = False):
            """ Attempts to list files from the given server_id.
                    - server_id,          REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
                    - pathway,            REQUIRED - YES | The path is counted from the root node as seen in the file manager in the control panel.
                    - hide_default_files, REQUIRED - NO  | Won't return default files if true.
                    - with_filesizes,     REQUIRED - NO  | Will return filesizes if true.
            """

            params = {'hide_default_files': hide_default_files, 'path': path, 'with_filesizes': with_filesizes}

            async with self.session.get('{}/game-servers/{}/files'.format(self.route, server_id), params=params) as r:
                if r.status == 200:
                    data = await r.json()
                else:
                    data = False

            return data

    class console:
        """
        Game server console interactions.
        """

        async def pull(self, server_id, max_lines = 1):
            """ Attempts to pull X amount of lines from the console for the given server_id.
                    - server_id, REQUIRED - YES | Dathost's ID used to uniquely identify a game server. 
                    - max_lines, REQUIRED - NO  | Default 1.
            """

            params = {'max_lines': max_lines}

            async with self.session.get('{}/game-servers/{}/console'.format(self.route, server_id), params=params) as r:
                if r.status == 200:
                    data = await r.read()
                else:
                    data = False

            return data

        async def send(self, server_id, console_line):
            """ Attempts to send a single line of text to the console for the given server_id.
                    - server_id, REQUIRED - YES    | Dathost's ID used to uniquely identify a game server. 
                    - console_line, REQUIRED - YES | Single line of text to send to the console.
            """

            params = {'line': console_line}

            async with self.session.post('{}/game-servers/{}/console'.format(self.route, server_id), params=params) as r:
                data = r.status == 200

            return data

    async def domains(self):
        """ 
        Attempts to pull Dathost's domains.
        """
        async with self.session.get('{}/custom-domains'.format(self.route)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def account(self):
        """
        Returns account infomation.
        """

        async with self.session.get('{}/account'.format(self.route)) as r:
            if r.status == 200:
                data = await r.json()
            else:
                data = False

        return data

    async def details(self):
        """
        Returns full list of details about all the game servers currently not deleted in this account.
        """

        async with self.session.get('{}/game-servers'.format(self.route)) as r:
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