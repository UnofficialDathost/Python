from datetime import datetime


class BackupModel:
    """Holds detail on backups.

    Attributes
    ----------
    backup_name : str
    timestamp : datetime.datetime
    """

    def __init__(self, data: dict) -> None:
        self.backup_name = data["name"]
        self.timestamp = datetime.strptime(
            data["timestamp"],
            "%a %b %d %H:%M %Y"
        )
