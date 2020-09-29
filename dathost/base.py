from httpx import BasicAuth


class Base:
    def __init__(self, email: str, password: str, timeout: int = 60) -> None:
        """Used to create Dathost basic auth.

        Parameters
        ----------
        email : str
            Email of dathost account.
        password : str
            Password of dathost account.
        timeout : int, optional
            by default 60
        """

        self._basic_auth = BasicAuth(email, password)
        self._timeout = timeout
