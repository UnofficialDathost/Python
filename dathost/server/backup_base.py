class BackupBase:
    def __init__(self, context: object, server_id: str,
                 backup_name: str) -> None:

        self.backup_name = backup_name
        self.context = context
        self.server_id = server_id
