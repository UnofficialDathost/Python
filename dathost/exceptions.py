class InvalidSlotSize(Exception):
    """Raised when slot size is invalid.
    """

    pass


class MultipleGames(Exception):
    """Raised when you attempt to create one server
       with multiple games.
    """

    pass


class InvalidTickrate(Exception):
    """Raised when tickrate is invalid.
    """

    pass


class InvalidConsoleLine(Exception):
    """Raised when console line is above 1 or above 100000.
    """

    pass


class AwaitingOnly(Exception):
    """Raised when a coroutine called is awaiting supported only.
    """

    pass


class InvalidSteamID(Exception):
    """Raised when give ID isn't understood.
    """

    pass


class NotFound(Exception):
    """Resource not found.
    """

    pass


class BadRequest(Exception):
    """Path is a directory or Cannot move file into itself.
    """

    pass


class ExceededStorage(Exception):
    """Your disk quota of 30GB per server (excluding base installation)
    has been exceeded
    """

    pass


class ServerStart(Exception):
    """Failed to start server.
    """

    pass
