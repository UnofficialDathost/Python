class Files(object):
    def __init__(self, server_id, pathway, force_sync, obj):
        self.obj = obj
        self.server_id = server_id
        self.pathway = pathway
        self.force_sync = force_sync

    async def sync(self):
        """ Attempts to sync files for the server. """

        return await self.obj._post(url=self.obj.routes["server"]["file"]["sync"].format(self.server_id))

    async def list(self, hide_default_files=False, with_filesizes=False):
        """ Attempts to list files from the server.
                - hide_default_files, default False
                - with_filesizes, default False
                - force_sync, default False | Force's dathost to re-cache.
        """

        if self.force_sync:
            await self.sync()

        params = {
            "hide_default_files": str(hide_default_files).lower(), 
            "path": self.pathway, 
            "with_filesizes": str(with_filesizes).lower(),
        }

        return await self.obj._get(url=self.obj.routes["server"]["file"]["list"].format(self.server_id),
                                   params=params)


    async def download(self):
        """ Attempts to download a file from the server. 
                - force_sync, default False | Force's dathost to re-cache.
        """

        if self.force_sync:
            await self.sync()

        return await self.obj._get(return_read=True, url=self.obj.routes["server"]["file"]["download"].format(self.server_id, self.pathway))

    async def delete(self):
        """ Attempts to delete a file from the server. 
            WARNING: THE DELETE FILE WILL BE DELETED! (dah)
            
            - force_sync, default False | Force's dathost to re-cache.
        """

        if self.force_sync:
            await self.sync()

        return await self.obj._delete(url=self.obj.routes["server"]["file"]["delete"].format(self.server_id, self.pathway))

    async def unzip(self):
        """ Attempts to upzip a file on the server. """

        return await self.obj._post(url=self.obj.routes["server"]["file"]["unzip"].format(self.server_id, self.pathway))

    async def upload(self, data: bytes):
        """ Attempts to upload a file to the server.
                - data, bytes to upload (max 500 mbs).
        """

        return await self.obj._post(url=self.obj.routes["server"]["file"]["upload"].format(self.server_id, self.pathway), data=data)