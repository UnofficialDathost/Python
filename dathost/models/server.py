from datetime import datetime
from typing import Generator


class PortsModel:
    """Holds details on ports

    Attributes
    ----------
    game : int
    gotv : int
    """

    def __init__(self, data: dict) -> None:
        self.game = data["game"]
        self.gotv = data["gotv"]


class ScheduledCommandsModel:
    """Holds details on scheduled commands

    Attributes
    ----------
    name : str
    action : str
    command : str
    run_at : str
    repeat : bool
    """

    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.action = data["action"]
        self.command = data["command"]
        self.run_at = data["run_at"]
        self.repeat = data["repeat"]


class ValheimModel:
    """Holds details on valheim server

    Attributes
    ----------
    admins : List[Int]
    plus : bool
    slots : int
    password : str
    world_name : str
    """

    def __init__(self, data: dict) -> None:
        self.admins = data["admins_steamid64"]
        self.plus = data["enable_valheimplus"]
        self.slots = data["slots"]
        self.password = data["password"]
        self.world_name = data["world_name"]


class TeamspeakModel:
    """Holds details on teamspeak server

    Attributes
    ----------
    slots : int
    admin_token : str
    """

    def __init__(self, data: dict) -> None:
        self.slots = data["slots"]
        self.admin_token = data["ts_admin_token"]


class TeamFortressModel:
    """Holds details on tf2.

    Attributes
    ----------
    slots : int
    rcon : str
    password : str
    admins : str
    gotv : bool
    sourcemod : bool
    insecure : bool
    """

    def __init__(self, data: dict) -> None:
        self.slots = data["slots"]
        self.rcon = data["rcon"]
        self.password = data["password"]
        self.admins = data["sourcemod_admins"]
        self.gotv = data["enable_gotv"]
        self.sourcemod = data["enable_sourcemod"]
        self.insecure = data["insecure"]


class CsgoModel:
    """Holds details on csgo server

    Attributes
    ----------
    slots : int
    game_token : str
    rcon : str
    password : str
    maps_source : str
    map_group : str
    map_group_start_map : str
    workshop_id : str
    workshop_start_map_id : str
    steam_key : str
    autoload_configs : list
    admins : str
    plugins : list
    gotv : bool
    sourcemod : bool
    csay_plugin : bool
    game_mode : str
    tickrate : int
    pure : bool
    insecure : bool
    disable_bots: bool
    """

    def __init__(self, data: dict) -> None:
        self.slots = data["slots"]
        self.game_token = data["steam_game_server_login_token"]
        self.rcon = data["rcon"]
        self.password = data["password"]
        self.maps_source = data["maps_source"]
        self.map_group = data["mapgroup"]
        self.map_group_start_map = data["mapgroup_start_map"]
        self.workshop_id = data["workshop_id"]
        self.workshop_start_map_id = data["workshop_start_map_id"]
        self.steam_key = data["workshop_authkey"]
        self.autoload_configs = data["autoload_configs"]
        self.admins = data["sourcemod_admins"]
        self.plugins = data["sourcemod_plugins"]
        self.gotv = data["enable_gotv"]
        self.sourcemod = data["enable_sourcemod"]
        self.csay_plugin = data["enable_csay_plugin"]
        self.game_mode = data["game_mode"]
        self.tickrate = data["tickrate"]
        self.pure = data["pure_server"]
        self.insecure = data["insecure"]
        self.disable_bots = data["disable_bots"]


class ServerModel:
    """Holds details on server

    Attributes
    ----------
    server_id : str
    name : str
    user_data : str
    match_id : str
    game : str
    location : str
    players_online : int
    status : list
    booting : bool
    server_error : str
    ip : str
    raw_ip : str
    on : bool
    ports : PortsModel
    confirmed : bool
    cost_per_hour : int
    max_cost_per_hour : int
    month_credits : float
    month_reset_at : datetime
    max_cost_per_month : float
    subscription_cycle_months : int
    subscription_renewal_failed_attempts : int
    mysql : bool
    autostop : bool
    autostop_minutes : int
    mysql_username : str
    mysql_password : str
    ftp_password : str
    disk_usage_bytes : int
    default_file_locations : list
    custom_domain :  str
    added_voice_server : str
    duplicate_source_server : str
    teamspeak : TeamspeakModel
    teamfortress : TeamFortressModel
    valheim : ValheimModel
    csgo : CsgoModel
    max_disk_usage_gb : int
    reboot_on_crash : bool
    core_dump : bool
    prefer_dedicated : bool
    """

    def __init__(self, data: dict) -> None:
        self.server_id = data["id"]
        self.name = data["name"]
        self.user_data = data["user_data"]
        self.match_id = data["match_id"]
        self.game = data["game"]
        self.location = data["location"]
        self.players_online = data["players_online"]
        self.status = data["status"]
        self.booting = data["booting"]
        self.server_error = data["server_error"]
        self.ip = data["ip"]
        self.raw_ip = data["raw_ip"]
        self.on = data["on"]
        self.ports = PortsModel(data["ports"])
        self.confirmed = data["confirmed"]
        self.reboot_on_crash = data["reboot_on_crash"]
        self.max_disk_usage_gb = data["max_disk_usage_gb"]
        self.core_dump = data["enable_core_dump"]
        self.cost_per_hour = data["cost_per_hour"]
        self.max_cost_per_hour = data["max_cost_per_hour"]
        self.month_credits = data["month_credits"]
        self.month_reset_at = datetime.fromtimestamp(data["month_reset_at"])
        self.max_cost_per_month = data["max_cost_per_month"]
        self.subscription_cycle_months = data["subscription_cycle_months"]
        self.subscription_renewal_failed_attempts = (
            data["subscription_renewal_failed_attempts"]
        )
        self.mysql = data["enable_mysql"]
        self.autostop = data["autostop"]
        self.autostop_minutes = data["autostop_minutes"]
        self.mysql_username = data["mysql_username"]
        self.mysql_password = data["mysql_password"]
        self.ftp_password = data["ftp_password"]
        self.disk_usage_bytes = data["disk_usage_bytes"]
        self.default_file_locations = data["default_file_locations"]
        self.custom_domain = data["custom_domain"]
        self.added_voice_server = data["added_voice_server"]
        self.duplicate_source_server = data["duplicate_source_server"]
        self.prefer_dedicated = data["prefer_dedicated"]

        self.teamspeak = TeamspeakModel(
            data["teamspeak3_settings"]
        ) if data["teamspeak3_settings"] else None
        self.teamfortress = TeamFortressModel(
            data["teamfortress2_settings"]
        ) if data["teamfortress2_settings"] else None
        self.csgo = CsgoModel(
            data["csgo_settings"]
        ) if data["csgo_settings"] else None
        self.valheim = ValheimModel(
            data["valheim_settings"]
        ) if data["valheim_settings"] else None

        self.__scheduled_commands = data["scheduled_commands"]

    def scheduled_commands(self
                           ) -> Generator[ScheduledCommandsModel, None, None]:
        """Lists scheduled commands.

        Yields
        ------
        ScheduledCommandsModel
            Holds data on scheduled commands.
        """

        for data in self.__scheduled_commands:
            yield ScheduledCommandsModel(data)
