import typing


class MapsModel:
    def __init__(self, data: dict) -> None:
        self.map = data["map"]
        self.seconds = data["seconds"]


class PlayerModel:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.duration = data["duration"]
        self.score = data["score"]


class PlayersOnlineGraphModel:
    def __init__(self, data: dict) -> None:
        self.timestamp = data["timestamp"]
        self.value = data["value"]


class MetricsModel:
    def __init__(self, data: dict) -> None:
        self.data = data

    def maps(self) -> typing.AsyncGenerator[MapsModel, None]:
        """Used to list all maps what have been played.

        Yields
        -------
        MapsModel
            Holds details on maps.
        """

        for data in self.data["maps_played"]:
            yield MapsModel(data)

    def players_online(self
                       ) -> typing.AsyncGenerator[PlayerModel, None]:
        """Used to list all players online.

        Yields
        -------
        PlayerModel
            Holds details on online players.
        """

        for data in self.data["players_online"]:
            yield PlayerModel(data)

    def players_online_graph(self) \
            -> typing.AsyncGenerator[PlayersOnlineGraphModel, None]:
        """Used to list all players online graph.

        Yields
        -------
        PlayersOnlineGraphModel
            Holds details on online player times.
        """

        for data in self.data["players_online_graph"]:
            yield PlayersOnlineGraphModel(data)

    def all_time_players(self) \
            -> typing.AsyncGenerator[PlayerModel, None]:
        """Used to list all time players.

        Yields
        -------
        PlayerModel
            Holds details on online players.
        """

        for data in self.data["all_time_players"]:
            yield PlayerModel(data)
