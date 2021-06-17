import aiofiles
from typing import AsyncGenerator, cast, TYPE_CHECKING

from ...routes import SERVER
from ..base import FileBase

if TYPE_CHECKING:
    from ... import Awaiting


class AwaitingFile(FileBase):
    _context: "Awaiting"

    async def delete(self) -> None:
        """Deletes file.
        """

        await self._context._delete(
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

        await self._context._put(
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

        await self._context._post(
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

    async def upload(self, data: bytes = None) -> None:
        """Used for uploading raw bytes.

        Parameters
        ----------
        data : bytes
            Data to upload.
        """

        await self._context._post(
            url=SERVER._upload.format(self.server_id, self.file_path),
            files={
                "file": data,
            },
        )

    async def save(self, local_pathway: str) -> None:
        """Saves file to local pathway.

        Parameters
        ----------
        local_pathway : str
            Pathway to save file to.
        """

        async with aiofiles.open(local_pathway, "wb+") as f:
            async for data in self.download_iterate():
                await f.write(data)

    async def download_iterate(self
                               ) -> AsyncGenerator[bytes, None]:
        """Asynchronously downloads data into memory.

        Yields
        -------
        bytes
        """

        url = SERVER.file_interact.format(self.server_id, self.file_path)
        async for data in self._context._stream(url):
            yield data

    async def dowload(self) -> bytes:
        """Used to download a file into memory.

        Returns
        -------
        bytes

        Notes
        ------
        Its reccomened to use download_iterate for large files.
        """

        return cast(
            bytes,
            await self._context._get(
                SERVER.file_interact.format(self.server_id, self.file_path),
                read_bytes=True,
                read_json=False
            )
        )
