from .files import Files

class Server(object):
    def __init__(self, server_id, obj):
        self.obj = obj
        self.server_id = server_id

    async def get(self):
        """ Attempts to get server details. """

        return await self.obj._get(url=self.obj.routes["server"]["get"].format(self.server_id))

    async def start(self):
        """ Attempts to start the server. """

        return await self.obj._post(url=self.obj.routes["server"]["start"].format(self.server_id))

    async def reset(self):
        """ Attempts to reset the server. 

            WARNING: THIS COMPLETELY RESETS THE GAME SERVER TO ITS DEFAULT FILES!
        """

        return await self.obj._post(url=self.obj.routes["server"]["restart"].format(self.server_id))

    async def stop(self):
        """ Attempts to stop the server """

        return await self.obj._post(url=self.obj.routes["server"]["stop"])

    async def send_command(self, command):
        """ Attempts to send console command to server.
                - command, rcon command.
        """

        return await self.obj._post(url=self.obj.routes["server"]["console"]["send"].format(self.server_id), 
                                    params={"line": command,})

    async def console(self, max_lines:int =1):
        """ Attempts to pull X amount of lines from the server. 
                 - max_lines, How many lines to pull, default 1.
        """
        
        return await self.obj._get(url=self.obj.routes["server"]["console"]["get"].format(self.server_id),
                                   params={"max_lines": max_lines,})

    async def create(self, parameters: dict):
        """ Attempts to spawn a new server with the passed parameters. 
                - parameters, Expects a dictionary of server parameters.
        """

        return await self.obj._post(url=self.obj.routes["server"]["create"], params=parameters)

    async def delete(self):
        """ Attempts to delete the server. 

            WARNING: ALL FILES & USED CREDIT WILL BE LOST! 
        """

        return await self.obj._delete(url=self.obj.routes["server"]["delete"].format(self.server_id))

    async def ftp_regenerate(self):
        """ Attempts to generate a new FTP password for the server. """

        return await self.obj._post(url=self.obj.routes["server"]["ftp_password_reset"].format(self.server_id))

    def files(self, pathway="", force_sync=False):
        """ Object for server file interactions 
                - pathway, default root | pathway to file.
                - force_sync, default false | forces dathost to re-cache.
        """

        return Files(server_id=self.server_id, pathway=pathway, force_sync=force_sync, obj=self.obj)

    async def clone(self):
        """ Attempts to clone the server. """

        return await self.obj._post(url=self.obj.routes["server"]["clone"].format(self.server_id))

    async def metrics(self):
        """ Attempts to pull metrics for the server. """

        return await self.obj._post(url=self.obj.routes["server"]["metrics"].format(self.server_id))