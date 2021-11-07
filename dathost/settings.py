from __future__ import annotations
from typing import Any, List, Union

import json

from steam.steamid import SteamID

from .exceptions import (
    InvalidSlotSize,
    MultipleGames,
    InvalidTickrate,
    InvalidSteamID,
    InvalidStorageSize
)


VALID_TICKRATES = [
    64,
    85,
    100,
    102.4,
    128
]


def _format_admins(admins, format_32: bool = True) -> str:
    return json.dumps([
        SteamID(steam_id).as_steam2
        if format_32 else str(SteamID(steam_id).as_64)
        for steam_id in admins
    ])


class ServerSettings:
    __game = False

    def __init__(self, name: str = None, location: str = None,
                 custom_domain: str = None,
                 autostop: bool = None, autostop_minutes: int = None,
                 mysql: bool = None, scheduled_commands: List[str] = None,
                 user_data: str = None,
                 reboot_on_crash: bool = None,
                 max_disk_usage_gb: int = None,
                 manual_sort_order: int = None,
                 core_dump: bool = None,
                 prefer_dedicated: bool = None) -> None:
        """Used to store settings on a server.

        Parameters
        ----------
        name : str, optional
            Name of server, by default None
        location : str, optional
            Location of server, by default None
        custom_domain : str, optional
            Custom domain name, by default None
        autostop : bool, optional
            If autostop is enabled, by default None
        autostop_minutes : int, optional
            How many minutes, by default None
        mysql : bool, optional
            If myself is enabled, by default None
        scheduled_commands : List[str], optional
            List of scheduled commands, by default None
        user_data : str, optional
            User meta data, by default None
        reboot_on_crash : bool, optional
            by default None
        max_disk_usage_gb : int, optional
            by default None
        manual_sort_order : int, optional
            by default None
        core_dump : bool, optional
            by default None
        prefer_dedicated : bool, optional
            by default None
        """

        self.payload = {}

        if name is not None:
            self.payload["name"] = name
        if location is not None:
            self.payload["location"] = location
        if autostop is not None:
            self.payload["autostop"] = autostop
        if autostop_minutes is not None:
            self.payload["autostop_minutes"] = autostop_minutes
        if mysql is not None:
            self.payload["enable_mysql"] = mysql
        if reboot_on_crash is not None:
            self.payload["reboot_on_crash"] = reboot_on_crash
        if core_dump is not None:
            self.payload["enable_core_dump"] = core_dump
        if custom_domain is not None:
            self.payload["custom_domain"] = custom_domain
        if scheduled_commands is not None:
            self.payload["scheduled_commands"] = json.dumps(scheduled_commands)
        if user_data is not None:
            self.payload["user_data"] = user_data
        if manual_sort_order is not None:
            self.payload["manual_sort_order"] = manual_sort_order
        if max_disk_usage_gb is not None:
            if max_disk_usage_gb > 100 or max_disk_usage_gb < 30:
                raise InvalidStorageSize()

            self.payload["max_disk_usage_gb"] = max_disk_usage_gb
        if prefer_dedicated is not None:
            self.payload["prefer_dedicated"] = prefer_dedicated

    def csgo(self, slots: int = None, tickrate: int = None,
             game_token: str = None, rcon_password: str = None,
             game_mode: str = None, autoload_configs: List[str] = None,
             disable_bots: bool = False, workshop_start_map_id: int = None,
             csay_plugin: bool = False, gotv: bool = False,
             sourcemod: bool = False, insecure: bool = False,
             map_group: str = None, start_map: str = None,
             password: str = None, pure: bool = True,
             admins: List[Any] = None, plugins: List[Any] = None,
             steam_key: str = None,
             workshop_id: int = None, maps_source: str = None
             ) -> ServerSettings:
        """Used for configuring a CS: GO server.

        Parameters
        ----------
        slots : int
        game_token : str
        tickrate : int
        game_mode : str, optional
            by default None
        autoload_configs : List[str], optional
            by default None
        disable_bots : bool, optional
            by default False
        csay_plugin : bool, optional
            by default False
        gotv : bool, optional
            by default False
        sourcemod : bool, optional
            by default False
        insecure : bool, optional
            by default False
        map_group : str, optional
            by default None
        start_map : str, optional
            by default None
        password : str, optional
            by default None
        pure : bool, optional
            by default True
        rcon_password : str, optional
            by default None
        admins : List[Any], optional
            by default None
        plugins : List[Any], optional
            by default None
        steam_key : str, optional
            by default None
        workshop_id : int, optional
            by default None
        workshop_start_map_id : int, optional
            by default None
        maps_source : int, optional
            by default None

        Raises
        ------
        MultipleGames
            Raised when you attempt to create one server
            with multiple games.
        InvalidSlotSize
            Raised when slot size is below 5 or above 64.
        InvalidTickrate
            Raised when tickrate is invalid.

        Returns
        -------
        ServerSettings
        """

        if self.__game:
            raise MultipleGames()

        self.__game = True

        self.payload["game"] = "csgo"

        if autoload_configs is not None:
            self.payload[
                "csgo_settings.autoload_configs"
            ] = json.dumps(autoload_configs)
        if disable_bots is not None:
            self.payload["csgo_settings.disable_bots"] = disable_bots
        if csay_plugin is not None:
            self.payload[
                "csgo_settings.enable_csay_plugin"
            ] = csay_plugin
        if gotv is not None:
            self.payload["csgo_settings.enable_gotv"] = gotv
        if sourcemod is not None:
            self.payload["csgo_settings.enable_sourcemod"] = sourcemod
        if game_mode is not None:
            self.payload["csgo_settings.game_mode"] = game_mode
        if insecure is not None:
            self.payload["csgo_settings.insecure"] = insecure
        if map_group is not None:
            self.payload["csgo_settings.mapgroup"] = map_group
        if start_map is not None:
            self.payload["csgo_settings.mapgroup_start_map"] = start_map
        if password is not None:
            self.payload["csgo_settings.password"] = password
        if pure is not None:
            self.payload["csgo_settings.pure_server"] = pure
        if rcon_password is not None:
            self.payload["csgo_settings.rcon"] = rcon_password
        if slots is not None:
            if slots < 5 or slots > 64:
                raise InvalidSlotSize()

            self.payload["csgo_settings.slots"] = slots
        if admins is not None:
            self.payload[
                "csgo_settings.sourcemod_admins"
            ] = _format_admins(admins)

        if plugins is not None:
            self.payload[
                "csgo_settings.sourcemod_plugins"
            ] = json.dumps(plugins)
        if game_token is not None:
            self.payload[
                "csgo_settings.steam_game_server_login_token"
            ] = game_token
        if tickrate is not None:
            if tickrate not in VALID_TICKRATES:
                raise InvalidTickrate()
            self.payload["csgo_settings.tickrate"] = tickrate
        if steam_key is not None:
            self.payload["csgo_settings.workshop_authkey"] = steam_key
        if workshop_id is not None:
            self.payload["csgo_settings.workshop_id"] = workshop_id
        if workshop_start_map_id is not None:
            self.payload[
                "csgo_settings.workshop_start_map_id"
            ] = workshop_start_map_id
        if maps_source is not None:
            self.payload["csgo_settings.maps_source"] = maps_source

        return self

    def tf2(self, slots: int = None, rcon_password: str = None,
            gotv: bool = False, sourcemod: bool = False,
            insecure: bool = False, password: str = None,
            admins: list = None) -> ServerSettings:
        """Used for configuring a TF2 server.

        Parameters
        ----------
        rcon_password : str
        slots : int
        gotv : bool, optional
            by default False
        sourcemod : bool, optional
            by default False
        insecure : bool, optional
            by default False
        password : str, optional
            by default None
        admins : list, optional
            by default None

        Raises
        ------
        MultipleGames
            Raised when you attempt to create one server
            with multiple games.
        InvalidSlotSize
            Raised when slot size is below 5 or above 32.

        Returns
        -------
        ServerSettings
        """

        if self.__game:
            raise MultipleGames()

        self.__game = True

        self.payload["game"] = "teamfortress2"
        if slots is not None:
            if slots < 5 or slots > 32:
                raise InvalidSlotSize()

            self.payload["teamfortress2_settings.slots"] = slots
        if rcon_password is not None:
            self.payload["teamfortress2_settings.rcon"] = rcon_password
        if gotv is not None:
            self.payload["teamfortress2_settings.enable_gotv"] = gotv
        if sourcemod is not None:
            self.payload[
                "teamfortress2_settings.enable_sourcemod"
            ] = sourcemod
        if insecure is not None:
            self.payload["teamfortress2_settings.insecure"] = insecure
        if password is not None:
            self.payload["teamfortress2_settings.password"] = password
        if admins is not None:
            self.payload[
                "teamfortress2_settings.sourcemod_admins"
            ] = _format_admins(admins)

        return self

    def valheim(self, password: str = None, world_name: str = None,
                plus: bool = None, admins: List[Any] = None
                ) -> ServerSettings:
        """Used to configure valheim server.

        Parameters
        ----------
        password : str, optional
            by default None
        world_name : str, optional
            by default None
        plus : bool, optional
            by default None
        admins : List[Any], optional
            List of SteamIDs in any format, by default None

        Returns
        -------
        ServerSettings

        Raises
        ------
        MultipleGames
        """

        if self.__game:
            raise MultipleGames()

        self.__game = True

        self.payload["game"] = "valheim"
        if password is not None:
            self.payload["valheim_settings.password"] = password
        if world_name is not None:
            self.payload["valheim_settings.world_name"] = world_name
        if plus is not None:
            self.payload["valheim_settings.enable_valheimplus"] = plus
        if admins is not None:

            self.payload[
                "valheim_settings.admins_steamid64"
            ] = _format_admins(admins, format_32=False)

        return self

    def teamspeak(self, slots: int) -> ServerSettings:
        """Used for configuring a teamspeak server.

        Parameters
        ----------
        slots : int

        Raises
        ------
        MultipleGames
            Raised when you attempt to create one server
            with multiple games.
        InvalidSlotSize
            Raised when slot size is below 5 or above 500.

        Returns
        -------
        ServerSettings
        """

        if self.__game:
            raise MultipleGames()

        self.__game = True

        if slots < 5 or slots > 500:
            raise InvalidSlotSize()

        self.payload["game"] = "teamspeak3"
        self.payload["teamspeak3_settings.slots"] = slots

        return self


class MatchSettings:
    def __init__(self, connection_time: int = 300,
                 knife_round: bool = False,
                 wait_for_spectators: bool = True,
                 enable_pause: bool = False,
                 enable_ready: bool = False,
                 enable_tech_pause: bool = False,
                 ready_min_players: int = 1,
                 wait_for_coaches: bool = True,
                 warmup_time: int = 15) -> None:
        """Used to create a match.

        Parameters
        ----------
        connection_time : int, optional
            by default 300
        knife_round : bool, optional
            by default False
        wait_for_spectators : bool, optional
            by default True
        warmup_time : int, optional
            by default 15
        enable_pause : bool, optional
            by default False
        enable_ready : bool, optional
            by default False
        enable_tech_pause : bool, optional
            by default False
        ready_min_players : int, optional
            by default 1
        wait_for_coaches : bool, optional
            by default True
        """

        self.payload = {
            "connection_time": connection_time,
            "enable_knife_round": knife_round,
            "wait_for_spectators": wait_for_spectators,
            "warmup_time": warmup_time,
            "enable_pause": enable_pause,
            "enable_ready": enable_ready,
            "enable_tech_pause": enable_tech_pause,
            "ready_min_players": ready_min_players,
            "wait_for_coaches": wait_for_coaches
        }

    def __convert_id(self, given_id: Union[str, int]) -> str:
        """Converts any steamID format to 32.

        Parameters
        ----------
        given_id : Any
            Given steamID.

        Returns
        -------
        str
            SteamID32

        Raises
        ------
        InvalidSteamID
            Raised when the given ID isn't understood.
        """

        steam_id = SteamID(given_id)
        if not steam_id.is_valid():
            raise InvalidSteamID()

        return steam_id.as_steam2

    def __format_players(self, players: list) -> str:
        return ",".join([self.__convert_id(steam_id) for steam_id in players])

    def playwin(self, webhook: str = None) -> MatchSettings:
        """Enables playwin AC.

        Parameters
        ----------
        webhook : str, optional
            Webhook to push playwin results, by default None

        Returns
        -------
        MatchSettings
        """

        self.payload["enable_playwin"] = True
        if webhook is not None:
            self.payload["playwin_result_webhook_url"] = webhook

        return self

    def webhook(self, match_end: str, round_end: str,
                authorization: str = None) -> MatchSettings:
        """Used to set webhooks.

        Parameters
        ----------
        match_end : str
            URL of match end webhook.
        round_end : str
            URL of round end webhook.
        authorization : str, optional
            by default None

        Returns
        -------
        MatchSettings
        """

        self.payload["match_end_webhook_url"] = match_end
        self.payload["round_end_webhook_url"] = round_end

        if authorization is not None:
            self.payload["webhook_authorization_header"] = authorization

        return self

    def spectators(self, players: list) -> MatchSettings:
        """Spectators

        Parameters
        ----------
        players : list
            List of spectator steam IDs,
            steamID 64, 32 & u are supported.

        Returns
        -------
        MatchSettings
        """

        self.payload["spectator_steam_ids"] = self.__format_players(players)

        return self

    def team_1(self, players: list, coach: Union[str, int] = None
               ) -> MatchSettings:
        """Team 1 players

        Parameters
        ----------
        players : list
            List of spectator steam IDs,
            steamID 64, 32 & u are supported.
        coach : Union[str, int]
            Steam id of coach, by deafult None

        Returns
        -------
        MatchSettings
        """

        self.payload["team1_steam_ids"] = self.__format_players(players)
        if coach:
            self.payload["team1_coach_steam_id"] = self.__convert_id(coach)

        return self

    def team_2(self, players: list, coach: Union[str, int] = None
               ) -> MatchSettings:
        """Team 2 players

        Parameters
        ----------
        players : list
            List of spectator steam IDs,
            steamID 64, 32 & u are supported.
        coach : Union[str, int]
            Steam id of coach, by deafult None

        Returns
        -------
        MatchSettings
        """

        self.payload["team2_steam_ids"] = self.__format_players(players)
        if coach:
            self.payload["team2_coach_steam_id"] = self.__convert_id(coach)

        return self


class MatchMapSettings:
    def __init__(self, map: str = "de_dust2", start_ct: int = 1) -> None:
        """Used to add maps

        Parameters
        ----------
        map : str, optional
            by default "de_dust2"
        start_ct : int, optional
            by default 1
        """

        self.map = map
        self.start_ct = f"team{start_ct}"


class MatchSeriesSettings:
    def __init__(self, match: MatchSettings,
                 message_prefix: str = None,
                 wait_for_gotv_before_nextmap: bool = None,
                 team_1_flag: str = None,
                 team_2_flag: str = None,
                 match_series_end_webhook_url: str = None) -> None:
        self.payload = match.payload

        if message_prefix is not None:
            self.payload["message_prefix"] = message_prefix
        if wait_for_gotv_before_nextmap is not None:
            self.payload["wait_for_gotv_before_nextmap"] = (
                wait_for_gotv_before_nextmap
            )
        if team_1_flag is not None:
            self.payload["team1_flag"] = team_1_flag
        if team_2_flag is not None:
            self.payload["team2_flag"] = team_1_flag
        if match_series_end_webhook_url is not None:
            self.payload["match_series_end_webhook_url"] = (
                match_series_end_webhook_url
            )

    def maps(self, maps: List[MatchMapSettings]
             ) -> MatchSeriesSettings:

        maps_len = len(maps)
        for index in range(0, maps_len - 1):
            self.payload[f"map{index}_start_ct"] = maps[index].start_ct
            self.payload[f"map{index}"] = maps[index].map

        self.payload["number_of_maps"] = maps_len

        return self
