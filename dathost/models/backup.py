from datetime import datetime


class BackupModel:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.timestamp = datetime.strptime(
            data["timestamp"],
            "%a %b %d %H:%M %Y"
        )
