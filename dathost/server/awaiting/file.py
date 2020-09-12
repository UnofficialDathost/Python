from ...routes import SERVER

from ..file_base import FileBase


class File(FileBase):
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
        """

        await self.context._put(
            SERVER.file_interact.format(self.server_id, self.file_path),
            data={
                "destination": destination,
            }
        )

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

    async def upload(self) -> None:
        pass

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
        -----
        Its reccomened to use download_iterate for large files.
        """

        return await self.context._get(
            SERVER.file_interact.format(self.server_id, self.file_path),
            timeout=timeout
        )
