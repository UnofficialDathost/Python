from ...routes import SERVER

from ..base import FileBase

from ...exceptions import AwaitingOnly


class BlockingFile(FileBase):
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

        Notes
        ------
        When called the file_path changes to the given destination.
        """

        self.context._put(
            SERVER.file_interact.format(self.server_id, self.file_path),
            data={
                "destination": destination,
            }
        )

        self.file_path = destination

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

    def upload_file(self, local_pathway: str) -> None:
        """Used to upload a local file.

        Parameters
        ----------
        local_pathway : str
            Local file to upload.
        """

        with open(local_pathway, "rb") as f:
            self.upload(f.read())

    def upload(self, data: bytes) -> None:
        """Used for uploading raw bytes.

        Parameters
        ----------
        data : bytes
            Data to upload.
        """

        self.context._post(
            url=SERVER._upload.format(self.server_id, self.file_path),
            data={
                "file": data,
            },
        )

    def save(self, local_pathway: str) -> None:
        """Saves file to local pathway.

        Parameters
        ----------
        local_pathway : str
            Pathway to save file to.
        """

        with open(local_pathway, "wb+") as f:
            f.write(self.dowload())

    def download_iterate(self) -> None:
        """
        Raises
        ------
        AwaitingOnly
            This function is meant only for awaiting
            code.
        """

        # This only exists so API structure remains identical.
        raise AwaitingOnly()

    def dowload(self) -> bytes:
        """Used to download a file into memory.

        Returns
        -------
        bytes

        Notes
        -----
        Its reccomened to use download_iterate for large files.
        """

        return self.context._get(
            SERVER.file_interact.format(self.server_id, self.file_path),
            read_bytes=True,
            read_json=False
        )
