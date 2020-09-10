class Route:
    _ran = False
    _prefix = None

    def __init__(self, route: str = "https://dathost.net/api/0.1") -> None:
        """Used for formatting route objects.

        Parameters
        ----------
        route : str, optional
            URL of API, by default "https://dathost.net/api/0.1"
        """

        self.route = route

    def format(self) -> None:
        """Used to format URL.
        """

        if self._ran:
            return

        routes = [
            attr for attr in dir(self.__class__)
            if not callable(getattr(self.__class__, attr))
            and not attr.startswith("__")
            and not attr.startswith("_")
        ]

        for var_name in routes:
            value = "{}{}/{}".format(
                self.route,
                "/" + self._prefix if self._prefix else "",
                getattr(
                    self,
                    var_name
                )
            )

            if value[-1:] == "/":
                value = value[:-1]

            setattr(
                self,
                var_name,
                value
            )


class Account(Route):
    details = "account"


class CustomDomains(Route):
    details = "custom-domains"


class Server(Route):
    _prefix = "game-servers"

    create = ""
    delete = "{}"
    get = "{}"
    list = ""
    update = "{}"
    console = "{}/console"
    duplicate = "{}/duplicate"
    sync = "{}/sync-files"
    ftp = "{}/regenerate-ftp-password"


ACCOUNT = Account()
CUSTOM_DOMAINS = CustomDomains()
SERVER = Server()

for route in [ACCOUNT, CUSTOM_DOMAINS, SERVER]:
    route.format()
