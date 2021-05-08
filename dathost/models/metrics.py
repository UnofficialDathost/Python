from typing import Generator


class MapsModel:
    """Holds map details

    Attributes
    ----------
    map : str
    seconds : int
    """

    def __init__(self, data: dict) -> None:
        self.map = data["map"]
        self.seconds = data["seconds"]


class PlayerModel:
    """Holds player details

    Attributes
    ----------
    name : str
    duration : int
    score : int
    """

    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.duration = data["duration"]
        self.score = data["score"]


class PlayersOnlineGraphModel:
    """Holds player graph details

    Attributes
    ----------
    timestamp : str
    value : str
    """

    def __init__(self, data: dict) -> None:
        self.timestamp = data["timestamp"]
        self.value = data["value"]


class MetricsModel:
    def __init__(self, data: dict) -> None:
        self.__data = data

    def maps(self) -> Generator[MapsModel, None, None]:
        """Used to list all maps what have been played.

        Yields
        -------
        MapsModel
            Holds details on maps.
        """

        for data in self.__data["maps_played"]:
            yield MapsModel(data)

    def players_online(self) -> Generator[PlayerModel, None, None]:
        """Used to list all players online.

        Yields
        -------
        PlayerModel
            Holds details on online players.
        """

        for data in self.__data["players_online"]:
            yield PlayerModel(data)

    def players_online_graph(self) -> Generator[
            PlayersOnlineGraphModel, None, None]:
        """Used to list all players online graph.

        Yields
        -------
        PlayersOnlineGraphModel
            Holds details on online player times.
        """

        for data in self.__data["players_online_graph"]:
            yield PlayersOnlineGraphModel(data)

    def all_time_players(self) -> Generator[PlayerModel, None, None]:
        """Used to list all time players.

        Yields
        -------
        PlayerModel
            Holds details on online players.
        """

        for data in self.__data["all_time_players"]:
            yield PlayerModel(data)
