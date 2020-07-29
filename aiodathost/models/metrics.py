import typing
from datetime import datetime


class AllTimePlayersModel:
    def __init__(self, data) -> None:
        self.name = data["all_time_players"]["name"]
        self.duration = data["all_time_players"]["duration"]
        self.score = data["score"]["score"]


class PlayersOnlineModel:
    def __init__(self, data) -> None:
        self.name = data["players_online"]["name"]
        self.duration = data["players_online"]["duration"]
        self.score = data["players_online"]["score"]


class PlayersOnlineGraphModel:
    def __init__(self, data) -> None:
        self.timestamp = datetime.utcfromtimestamp(
            data["players_online_graph"]["timestamp"]
        )
        self.value = data["players_online_graph"]["value"]


class MapsPlayedModel:
    def __init__(self, data) -> None:
        self.map = data["maps_played"]["map"]
        self.seconds = data["maps_played"]["seconds"]


class MetricsModel:
    def __init__(self, data) -> None:
        self.data = data

    def all_time_players(self) -> typing.AsyncGenerator[typing.Any, None]:
        """
        All time players yield.

        Yields
        ------
        AllTimePlayersModel
        """

        for player in self.data["all_time_players"]:
            yield AllTimePlayersModel(player)

    def players_online(self) -> typing.AsyncGenerator[typing.Any, None]:
        """
        Players online yield.

        Yields
        ------
        PlayersOnlineModel
        """

        for player in self.data["players_online"]:
            yield PlayersOnlineModel(player)

    def players_online_graph(self) -> typing.AsyncGenerator[typing.Any, None]:
        """
        Players online graph yield.

        Yields
        ------
        PlayersOnlineGraphModel
        """

        for player in self.data["players_online_graph"]:
            yield PlayersOnlineGraphModel(player)

    def maps_played(self) -> typing.AsyncGenerator[typing.Any, None]:
        """
        Maps played yield.

        Yields
        ------
        MapsPlayedModel
        """

        for map_name in self.data["maps_played"]:
            yield MapsPlayedModel(map_name)
