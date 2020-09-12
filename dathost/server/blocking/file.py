from ...routes import SERVER

from ..file_base import FileBase

from ...exceptions import AwaitingOnly


class File(FileBase):
    def delete(self) -> None:
        """Deletes file.
        """

        self.context._delete(
            SERVER.file_interact.format(self.server_id, self.file_path)
        )

    def move(self, destination: str) -> None:
        """Used for moving a file.

        Parameters
        ----------
        destination : str
        """

        self.context._put(
            SERVER.file_interact.format(self.server_id, self.file_path),
            data={
                "destination": destination,
            }
        )

    def unzip(self, destination: str) -> None:
        """Used to unzip a file.

        Parameters
        ----------
        destination : str
        """

        self.context._post(
            url=SERVER.file_unzip.format(self.server_id, self.file_path),
            data={
                "destination": destination,
            }
        )

    def upload(self) -> None:
        pass

    def download_iterate(self) -> None:
        """
        Raises
        ------
        AwaitingOnly
            This function is meant only for awaiting
            code.
        """

        raise AwaitingOnly()

    def dowload(self, timeout: int = 60) -> bytes:
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

        return self.context._get(
            SERVER.file_interact.format(self.server_id, self.file_path),
            timeout=timeout
        )
