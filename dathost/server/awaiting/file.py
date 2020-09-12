import typing
import aiofiles

from ...routes import SERVER

from ..file_base import FileBase


class AwaitingFile(FileBase):
    async def delete(self) -> None:
        """Deletes file.
        """

        await self.context._delete(
            SERVER.file_interact.format(self.server_id, self.file_path)
        )

    async def move(self, destination: str) -> None:
        """Used for moving a file.

        Parameters
        ----------
        destination : str

        Notes
        ------
        When called the file_path changes to the given destination.
        """

        await self.context._put(
            SERVER.file_interact.format(self.server_id, self.file_path),
            data={
                "destination": destination,
            }
        )

        self.file_path = destination

    async def unzip(self, destination: str) -> None:
        """Used to unzip a file.

        Parameters
        ----------
        destination : str
        """

        await self.context._post(
            url=SERVER.file_unzip.format(self.server_id, self.file_path),
            data={
                "destination": destination,
            }
        )

    async def upload_file(self, local_pathway: str) -> None:
        """Used to upload a local file.

        Parameters
        ----------
        local_pathway : str
            Local file to upload.
        """

        async with aiofiles.open(local_pathway, "rb") as f:
            await self.upload(await f.read())

    async def upload(self, data: bytes = None, timeout: int = 60) -> None:
        """Used for uploading raw bytes.

        Parameters
        ----------
        data : bytes
            Data to upload.
        timeout : int
            by default 60
        """

        await self.context._post(
            url=SERVER._upload.format(self.server_id, self.file_path),
            data={
                "file": data,
            },
            timeout=timeout
        )

    async def save(self, local_pathway: str, timeout: int = 60) -> None:
        """Saves file to local pathway.

        Parameters
        ----------
        local_pathway : str
            Pathway to save file to.
        timeout : int, optional
            by default 60
        """

        async with aiofiles.open(local_pathway, "wb+") as f:
            async for data in self.download_iterate(timeout=timeout):
                await f.write(data)

    async def download_iterate(self,  timeout: int = 60
                               ) -> typing.AsyncGenerator[bytes, None]:
        """Asynchronously downloads data into memory.

        Parameters
        ----------
        timeout : int, optional
            by default 60

        Yields
        -------
        bytes
        """

        url = SERVER.file_interact.format(self.server_id, self.file_path)
        async for data in self.context._stream(url, timeout=timeout):
            yield data

    async def dowload(self, timeout: int = 60) -> bytes:
        """Used to download a file into memory.

        Parameters
        ----------
        timeout : int, optional
            by default 60

        Returns
        -------
        bytes

        Notes
        ------
        Its reccomened to use download_iterate for large files.
        """

        return await self.context._get(
            SERVER.file_interact.format(self.server_id, self.file_path),
            timeout=timeout,
            read_bytes=True,
            read_json=False
        )
