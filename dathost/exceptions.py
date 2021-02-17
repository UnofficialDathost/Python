class DathostException(Exception):
    """Base exception for dathost.
    """

    def __init__(self, msg="Dathost base exception", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class InvalidSlotSize(DathostException):
    """Raised when slot size is invalid.
    """

    def __init__(self, msg="Invalid slot size", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class MultipleGames(DathostException):
    """Raised when you attempt to create one server
       with multiple games.
    """

    def __init__(self, msg="Multiple games called", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class InvalidTickrate(DathostException):
    """Raised when tickrate is invalid.
    """

    def __init__(self, msg="Invalid tickrate", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class InvalidConsoleLine(DathostException):
    """Raised when console line is above 1 or above 100000.
    """

    def __init__(self, msg="Invalid console line", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class AwaitingOnly(DathostException):
    """Raised when a coroutine called is awaiting supported only.
    """

    def __init__(self, msg="Only awaiting supported", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class InvalidSteamID(DathostException):
    """Raised when give ID isn't understood.
    """

    def __init__(self, msg="Invalid Steam ID", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class NotFound(DathostException):
    """Resource not found.
    """

    def __init__(self, msg="Resource not found", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class BadRequest(DathostException):
    """Path is a directory or Cannot move file into itself.
    """

    def __init__(self, msg="Bad request", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class ExceededStorage(DathostException):
    """Your disk quota of 30GB per server (excluding base installation)
    has been exceeded
    """

    def __init__(self, msg="Storage exceeded", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class ServerStart(DathostException):
    """Failed to start server.
    """

    def __init__(self, msg="Failed to start server", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)


class InvalidStorageSize(DathostException):
    """Storage size is invalid.
    """

    def __init__(self, msg="Storage size is invalid", *args, **kwargs) -> None:
        super().__init__(msg, *args, **kwargs)
