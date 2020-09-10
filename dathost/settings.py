from .gamemodes import COMPETITIVE
from .map_source import MAP_GROUP

from .exceptions import InvalidSlotSize, MultipleGames, InvalidTickrate


VALID_TICKRATES = [
    64,
    85,
    100,
    102.4,
    128
]


class ServerSettings:
    __game = False

    def __init__(self, name: str, location: str,
                 custom_domain: str = None,
                 autostop: bool = False, autostop_minutes: int = 0,
                 mysql: bool = False, scheduled_commands: list = None,
                 user_data: str = None) -> None:
        """Used to store settings on a server.

        Parameters
        ----------
        name : str
            Name of server.
        location : str
            Location of server.
        custom_domain : str, optional
            Custom domain name, by default None
        autostop : bool, optional
            If autostop is enabled, by default False
        autostop_minutes : int, optional
            How many minutes, by default 0
        mysql : bool, optional
            If myself is enabled, by default False
        scheduled_commands : list, optional
            List of scheduled commands, by default None
        user_data : str, optional
            User meta data, by default None
        """

        self.playload = {
            "name": name,
            "location": location,
            "autostop": autostop,
            "autostop_minutes": autostop_minutes,
            "enable_mysql": mysql,
        }

        if custom_domain:
            self.playload["custom_domain"] = custom_domain

        if scheduled_commands:
            self.playload["scheduled_commands"] = scheduled_commands

        if user_data:
            self.playload["user_data"] = user_data

    def csgo(self, slots: int, game_token: str, tickrate: int,
             rcon_password: str, game_mode: str = COMPETITIVE,
             autoload_configs: list = None, disable_bots: bool = False,
             enable_csay_plugin: bool = False, enable_gotv: bool = False,
             enable_sourcemod: bool = False, insecure: bool = False,
             map_group: str = MAP_GROUP, start_map: str = None,
             password: str = None, pure: bool = True,
             admins: list = None, plugins: list = None, steam_key: str = None,
             workshop_id: int = None, workshop_start_map_id: int = None
             ) -> None:
        """Used for configuring a CS: GO server.

        Parameters
        ----------
        slots : int
        game_token : str
        tickrate : int
        game_mode : str, optional
            by default COMPETITIVE
        autoload_configs : list, optional
            by default None
        disable_bots : bool, optional
            by default False
        enable_csay_plugin : bool, optional
            by default False
        enable_gotv : bool, optional
            by default False
        enable_sourcemod : bool, optional
            by default False
        insecure : bool, optional
            by default False
        map_group : str, optional
            by default MAP_GROUP
        start_map : str, optional
            by default None
        password : str, optional
            by default None
        pure : bool, optional
            by default True
        rcon_password : str, optional
            by default None
        admins : list, optional
            by default None
        plugins : list, optional
            by default None
        steam_key : str, optional
            by default None
        workshop_id : int, optional
            by default None
        workshop_start_map_id : int, optional
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
        """

        if self.__game:
            raise MultipleGames()

        self.__game = True

        self.playload["game"] = "csgo"

        if autoload_configs:
            self.playload["csgo_settings.autoload_configs"] = autoload_configs

        self.playload["csgo_settings.disable_bots"] = disable_bots
        self.playload["csgo_settings.enable_csay_plugin"] = enable_csay_plugin
        self.playload["csgo_settings.enable_gotv"] = enable_gotv
        self.playload["csgo_settings.enable_sourcemod"] = enable_sourcemod
        self.playload["csgo_settings.game_mode"] = game_mode
        self.playload["csgo_settings.insecure"] = insecure
        self.playload["csgo_settings.mapgroup"] = map_group

        if start_map:
            self.playload["csgo_settings.mapgroup_start_map"] = start_map

        if password:
            self.playload["csgo_settings.password"] = password

        self.playload["csgo_settings.pure_server"] = pure
        self.playload["csgo_settings.rcon"] = rcon_password

        if slots < 5 or slots > 64:
            raise InvalidSlotSize()

        self.playload["csgo_settings.slots"] = slots

        if admins:
            self.playload["csgo_settings.sourcemod_admins"] = admins

        if plugins:
            self.playload["csgo_settings.sourcemod_plugins"] = plugins

        self.playload["csgo_settings.steam_game_server_login_token"] \
            = game_token

        if tickrate not in VALID_TICKRATES:
            raise InvalidTickrate()

        self.playload["csgo_settings.tickrate"] = tickrate

        if steam_key:
            self.playload["csgo_settings.workshop_authkey"] = steam_key

        if workshop_id:
            self.playload["csgo_settings.workshop_id"] = workshop_id

        if workshop_start_map_id:
            self.playload["csgo_settings.workshop_start_map_id"] \
                = workshop_start_map_id

        return self

    def mumble(self, slots: int, superuser_password: str,
               password: str = None, motd: str = None) -> None:
        """Used for configuring a Mumble server.

        Parameters
        ----------
        slots : int
        superuser_password : str
        password : str, optional
            by default None
        motd : str, optional
            by default None

        Raises
        ------
        MultipleGames
            Raised when you attempt to create one server
            with multiple games.
        InvalidSlotSize
            Raised when slot size is below 7 or above 700.
        """

        if self.__game:
            raise MultipleGames()

        if slots < 7 or slots > 700:
            raise InvalidSlotSize()

        self.playload["game"] = "mumble"
        self.playload["mumble_settings.slots"] = slots
        self.playload["mumble_settings.superuser_password"] = \
            superuser_password

        if password:
            self.playload["mumble_settings.password"] = password

        if motd:
            self.playload["mumble_settings.welcome_text"] = motd

        return self

    def tf2(self, slots: int, rcon_password: str,
            gotv: bool = False, sourcemod: bool = False,
            insecure: bool = False, password: str = None,
            admins: list = None) -> None:
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
        """

        if self.__game:
            raise MultipleGames()

        if slots < 5 or slots > 32:
            raise InvalidSlotSize()

        self.playload["game"] = "teamfortress2"
        self.playload["teamfortress2_settings.rcon"] = rcon_password
        self.playload["teamfortress2_settings.enable_gotv"] = gotv
        self.playload["teamfortress2_settings.enable_sourcemod"] = sourcemod
        self.playload["teamfortress2_settings.insecure"] = insecure

        if password:
            self.playload["teamfortress2_settings.password"] = password

        if admins:
            self.playload["teamfortress2_settings.sourcemod_admins"] = admins

        return self

    def teamspeak(self, slots: int) -> None:
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
        """

        if self.__game:
            raise MultipleGames()

        if slots < 5 or slots > 500:
            raise InvalidSlotSize()

        self.playload["game"] = "teamspeak3"
        self.playload["teamspeak3_settings.slots"] = slots

        return self
