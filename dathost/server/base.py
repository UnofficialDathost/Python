from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import Awaiting, Blocking


class ServerBase:
    def __init__(self, context: Union["Awaiting", "Blocking"],
                 server_id: str) -> None:
        """Used to interact with a server.

        Parameters
        ----------
        context : object
            Context of the client.
        server_id : str
            Dathost server ID.
        """

        self._context = context
        self.server_id = server_id


class FileBase:
    def __init__(self, context: Union["Awaiting", "Blocking"],
                 server_id: str, file_path: str) -> None:
        self._context = context
        self.server_id = server_id
        self.file_path = file_path


class BackupBase:
    def __init__(self, context: Union["Awaiting", "Blocking"], server_id: str,
                 backup_name: str) -> None:
        self.backup_name = backup_name
        self._context = context
        self.server_id = server_id
