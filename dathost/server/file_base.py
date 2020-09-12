class FileBase:
    def __init__(self, context: object,
                 server_id: str, file_path: str) -> None:
        self.context = context
        self.server_id = server_id
        self.file_path = file_path
