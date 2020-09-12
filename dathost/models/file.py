class FileModel:
    def __init__(self, data: dict) -> None:
        self.path = data["path"]
        self.size = data["size"] if "size" in data else None
