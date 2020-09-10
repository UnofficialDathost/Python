from httpx import BasicAuth


class Base:
    def __init__(self, email: str, password: str) -> None:
        """Used to create Dathost basic auth.

        Parameters
        ----------
        email : str
            Email of dathost account.
        password : str
            Password of dathost account.
        """

        self._basic_auth = BasicAuth(email, password)
