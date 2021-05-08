from typing import Generator


class TeamModel:
    """Holds details on team.

    Attributes
    ----------
    score : int
    players : list
    """

    def __init__(self, players: list, score: int) -> None:
        self.score = score
        self.players = players


class MatchPlayerModel:
    """Holds match player details.

    Attributes
    ----------
    steamid : str
    kills : int
    deaths : int
    assists : int
    kdr : float
    """

    def __init__(self, data: dict) -> None:
        self.steamid = data["steam_id"]
        self.kills = data["kills"]
        self.deaths = data["deaths"]
        self.assists = data["assists"]

    @property
    def kdr(self) -> float:
        return (
            round(self.kills / self.deaths, 2)
            if self.kills > 0 and self.deaths > 0 else 0.00
        )


class MatchModel:
    """Holds match details.

    Attributes
    ----------
    match_id : str
    server_id : str
    connect_time : int
    round_end_webhook : str
    match_end_webhook : str
    finished : bool
    cancel_reason : str
    rounds_played : int
    spectators : list
    team_1 : TeamModel
    team_2 : TeamModel
    knife_round : bool
    playwin : bool
    playwin_webhook : str
    playwin_result : dict
    warmup_time : int
    wait_for_spectators : bool
    """
    def __init__(self, data: dict) -> None:
        self.match_id = data["id"]
        self.server_id = data["game_server_id"]
        self.connect_time = data["connect_time"]
        self.round_end_webhook = data["round_end_webhook_url"]
        self.match_end_webhook = data["match_end_webhook_url"]
        self.finished = data["finished"]
        self.cancel_reason = data["cancel_reason"]
        self.rounds_played = data["rounds_played"]
        self.spectators = data["spectator_steam_ids"]
        self.knife_round = data["enable_knife_round"]
        self.playwin = data["enable_playwin"]
        self.playwin_webhook = data["playwin_result_webhook_url"]
        self.playwin_result = data["playwin_result"]
        self.warmup_time = data["warmup_time"]
        self.wait_for_spectators = data["wait_for_spectators"]

        self.team_1 = TeamModel(
            data["team1_steam_ids"],
            data["team1_stats"]["score"]
        )
        self.team_2 = TeamModel(
            data["team2_steam_ids"],
            data["team2_stats"]["score"]
        )

        self.__players = data["player_stats"]

    def players(self) -> Generator[MatchPlayerModel, None, None]:
        """Used to list players.

        Yields
        -------
        PlayerModel
            Holds details on player.
        """

        for player in self.__players:
            yield MatchPlayerModel(player)
