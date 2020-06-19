class InvalidAuthorization(Exception):
    """
    Invalid authorization was given.
    """
    pass


class BadRequest(Exception):
    """
    Bad request was sent.
    """
    pass


class NotFound(Exception):
    """
    ID was not found.
    """
    pass


class AboveDiskQuota(Exception):
    """
    Your disk quota of 30GB per server
    (excluding base installation) has been exceeded.
    """
    pass


class InvalidMaxLines(Exception):
    """
    Lines can only be between 1 & 1,000.
    """
    pass


class RequestTimeout(Exception):
    """
    Dathost timed out our request.
    """
    pass


class InternalError(Exception):
    """
    An internal error occurred on dathost's end.
    """
    pass


class UndefinedError(Exception):
    """
    An error aiodathost can't understand
    was passed.
    """
    pass
