class ServerBase:
    def __init__(self, context: object, server_id: str) -> None:
        """Used to interact with a server.

        Parameters
        ----------
        context : object
            Context of the client.
        server_id : str
            Dathost server ID.
        """

        self.context = context
        self.server_id = server_id


class FileBase:
    def __init__(self, context: object,
                 server_id: str, file_path: str) -> None:
        self.context = context
        self.server_id = server_id
        self.file_path = file_path


class BackupBase:
    def __init__(self, context: object, server_id: str,
                 backup_name: str) -> None:

        self.backup_name = backup_name
        self.context = context
        self.server_id = server_id
