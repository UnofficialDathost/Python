class Routes:
    _route = "https://dathost.net/api/0.1"

    server_start = "game-servers/{}/start"
    server_restart = "game-servers/{}/reset"
    server_create = "game-servers"
    server_stop = "game-servers/{}/stop"
    server_delete = "game-servers/{}"
    server_get = "game-servers/{}"
    server_list = "game-servers"
    server_metrics = "game-servers/{}/metrics"
    server_clone = "game-servers/{}/duplicate"

    file_delete = "game-servers/{}/files/{}"
    file_sync = "game-servers/{}/sync-files"
    file_upload = "game-servers/{}/files/{}"
    file_unzip = "game-servers/{}/unzip/{}"
    file_list = "game-servers/{}/files"
    file_download = "game-servers/{}/files/{}"

    console_get = "game-servers/{}/console"
    console_send = "game-servers/{}/console"

    ftp_password_reset = "game-servers/{}/regenerate-ftp-password"

    domains = "custom-domains"

    account = "account"

    def format_routes(self):
        """
        Formats dathost routes.
        """

        routes = [
            attr for attr in dir(Routes())
            if not callable(getattr(Routes(), attr))
            and not attr.startswith("__")
            and not attr.startswith("_")
        ]

        for route in routes:
            setattr(
                self,
                route,
                "{}/{}".format(
                    self._route,
                    getattr(
                        self,
                        route
                    )
                )
            )


ROUTES = Routes()
ROUTES.format_routes()
