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
