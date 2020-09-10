class ServerBase:
    def __init__(self, context: object, server_id: str) -> None:
        """Used to interact with a server.

        Parameters
        ----------
        context : object
            Context of the client.
        server_id : str
            Dathost server ID.
        """

        self.context = context
        self.server_id = server_id
