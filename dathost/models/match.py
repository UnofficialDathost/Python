from typing import Generator


class TeamModel:
    """Holds details on team.

    Attributes
    ----------
    score : Optional[int]
    players : list
    flag: Optional[str]
    start_ct: bool
        by default False
    """

    def __init__(self, players: list, score: int = None) -> None:
        self.score = score
        self.players = players
        self.flag = None
        self.start_ct = False


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
    enable_pause : bool
    enable_ready : bool
    enable_tech_pause : bool
    team_1_coach : str
    team_2_coach : str
    wait_for_coaches : bool
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
        self.enable_pause = data["enable_pause"]
        self.enable_ready = data["enable_ready"]
        self.enable_tech_pause = data["enable_tech_pause"]
        self.team_1_coach = data["team1_coach_steam_id"]
        self.team_2_coach = data["team2_coach_steam_id"]
        self.wait_for_coaches = data["wait_for_coaches"]

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


class MatchSeriesMatchModel(MatchModel):
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
    enable_pause : bool
    enable_ready : bool
    enable_tech_pause : bool
    team_1_coach : str
    team_2_coach : str
    wait_for_coaches : bool
    message_prefix : str
    wait_for_gotv_before_nextmap : bool
    match_series_id : str
    """

    def __init__(self, data: dict) -> None:
        super().__init__(data)

        self.team_1.flag = data["team1_flag"]
        self.team_2.flag = data["team2_flag"]
        self.team_1.start_ct = data["team1_start_ct"]
        self.message_prefix = data["message_prefix"]
        self.wait_for_gotv_before_nextmap = (
            data["wait_for_gotv_before_nextmap"]
        )
        self.match_series_id = data["match_series_id"]


class MatchSeriesModel:
    """Holds match details.

    Attributes
    ----------
    finished : bool
    series_id : str
    match_series_end_webhook_url : str
    team_1_matches_won : int
    team_2_matches_won : int
    """

    def __init__(self, data: dict) -> None:
        self.finished = data["finished"]
        self.series_id = data["id"]
        self.match_series_end_webhook_url = (
            data["match_series_end_webhook_url"]
        )
        self.team_1_matches_won = data["team1_stats"]["matches_won"]
        self.team_2_matches_won = data["team2_stats"]["matches_won"]

        self.__matches = data["matches"]

    def matches(self) -> Generator[MatchSeriesMatchModel, None, None]:
        for match in self.__matches:
            yield MatchSeriesMatchModel(match)
