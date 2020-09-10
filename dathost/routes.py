class Route:
    _ran = False

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
            setattr(
                self,
                var_name,
                "{}/{}".format(
                    self.route,
                    getattr(
                        self,
                        var_name
                    )
                )
            )


class Account(Route):
    details = "account"


class CustomDomains(Route):
    details = "custom-domains"


ACCOUNT = Account()
CUSTOM_DOMAINS = CustomDomains()

for route in [ACCOUNT, CUSTOM_DOMAINS]:
    route.format()
