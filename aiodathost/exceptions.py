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
