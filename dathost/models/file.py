class FileModel:
    """Used to hold details on file.

    Attributes
    ----------
    path : str
    size : str, optional
    """

    def __init__(self, data: dict) -> None:
        self.path = data["path"]
        self.size = data.get("size")
