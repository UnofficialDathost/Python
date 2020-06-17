from datetime import datetime


class AllTimePlayersModel:
    def __init__(self, data):
        self.name = data["all_time_players"]["name"]
        self.duration = data["all_time_players"]["duration"]
        self.score = data["score"]["score"]


class PlayersOnlineModel:
    def __init__(self, data):
        self.name = data["players_online"]["name"]
        self.duration = data["players_online"]["duration"]
        self.score = data["players_online"]["score"]


class PlayersOnlineGraphModel:
    def __init__(self, data):
        self.timestamp = datetime.utcfromtimestamp(
            data["players_online_graph"]["timestamp"]
        )
        self.value = data["players_online_graph"]["value"]


class MapsPlayedModel:
    def __init__(self, data):
        self.map = data["maps_played"]["map"]
        self.seconds = data["maps_played"]["seconds"]


class MetricsModel:
    def __init__(self, data):
        self.data = data

    def all_time_players(self):
        """
        All time players yield.
        """

        for player in self.data["all_time_players"]:
            yield AllTimePlayersModel(player)

    def players_online(self):
        """
        Players online yield.
        """

        for player in self.data["players_online"]:
            yield PlayersOnlineModel(player)

    def players_online_graph(self):
        """
        Players online graph yield.
        """

        for player in self.data["players_online_graph"]:
            yield PlayersOnlineGraphModel(player)

    def maps_played(self):
        """
        Maps played yield.
        """

        for map_name in self.data["maps_played"]:
            yield MapsPlayedModel(map_name)
