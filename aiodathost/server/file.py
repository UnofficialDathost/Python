from ..wrapped_requests import AWR
from ..routes import ROUTES

import aiofiles


class File:
    def __init__(self, server_id, pathway):
        self.server_id = server_id
        self.pathway = pathway

    async def unzip(self, destination: str):
        """
        Unzips given file.

        destination: str
            Pathway to move the zip file content to.
        """

        return await AWR(
            ROUTES.file_unzip.format(
                self.server_id,
                self.pathway
            )
        ).post()

    async def delete(self):
        """
        Deletes the given pathway.
        """

        return await AWR(
            ROUTES.file_delete.format(
                self.server_id,
                self.pathway
            )
        ).delete()

    async def download(self, as_text: bool = False):
        """
        Downloads the file into memory.

        as_text: bool
            If true, files up to 100kB will be returned as text/plain
            and bigger files will return an error.
        """

        return await AWR(
            ROUTES.file_download.format(
                self.server_id,
                self.pathway
            ),
            params={
                "as_text": str(as_text).lower(),
            }
        ).get(read=True)

    async def download_iterate(self, as_text: bool = False):
        """
        Iterates over downloading file.

        as_text: bool
            If true, files up to 100kB will be returned as text/plain
            and bigger files will return an error.

        Notes
        -----
        Uses chunk size passed in client.
        """

        request = AWR(
            ROUTES.file_download.format(
                self.server_id,
                self.pathway
            ),
            params={
                "as_text": str(as_text).lower(),
            }
        )

        async for data in request.get_stream():
            yield data

    async def save(self, local_pathway: str):
        """
        Saves file to local pathway.

        local_pathway: str
            Local pathway.

        Notes
        -----
        Uses download_iterate to avoid memory issues.
        """

        async with aiofiles.open(local_pathway, mode="wb") as file:
            async for data in self.download_iterate():
                await file.write(data)

    async def upload(self, data: bytes = None):
        """
        Uploads given data onto the given pathway.

        If no bytes passed just creates the file/directory.
        """

        if data:
            request = AWR(
                ROUTES.upload_url_file_upload.format(
                    self.server_id,
                    self.pathway
                ),
                data={
                    "file": data,
                }
            )
        else:
            request = AWR(
                ROUTES.upload_url_file_upload.format(
                    self.server_id,
                    self.pathway
                )
            )

        return await request.post()

    async def move(self, destination: str):
        """
        Moves file to given destination.

        destination: str
            Pathway to move the file to.
        """

        return await AWR(
            ROUTES.file_move.format(
                self.server_id,
                self.pathway
            ),
            params={
                "destination": destination,
            }
        ).put()
