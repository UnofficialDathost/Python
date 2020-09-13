import typing


class PortsModel:
    def __init__(self, data: dict) -> None:
        self.game = data["game"]
        self.gotv = data["gotv"]


class ScheduledCommandsModel:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.action = data["action"]
        self.command = data["command"]
        self.run_at = data["run_at"]
        self.repeat = data["repeat"]


class TeamspeakModel:
    def __init__(self, data: dict) -> None:
        self.slots = data["slots"]
        self.admin_token = data["ts_admin_token"]


class TeamFortressModel:
    def __init__(self, data: dict) -> None:
        self.slots = data["slots"]
        self.rcon = data["rcon"]
        self.password = data["password"]
        self.admins = data["sourcemod_admins"]
        self.gotv = data["enable_gotv"]
        self.sourcemod = data["enable_sourcemod"]
        self.insecure = data["insecure"]


class MumbleModel:
    def __init__(self, data: dict) -> None:
        self.slots = data["slots"]
        self.password = data["password"]
        self.superuser_password = data["superuser_password"]
        self.motd = data["welcome_text"]


class CsgoModel:
    def __init__(self, data: dict) -> None:
        self.slots = data["slots"]
        self.game_tokens = data["steam_game_server_login_token"]
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
    def __init__(self, data: dict) -> None:
        self.server_id = data["id"]
        self.name = data["name"]
        self.user_data = data["user_data"]
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
        self.cost_per_hour = data["cost_per_hour"]
        self.max_cost_per_hour = data["max_cost_per_hour"]
        self.month_credits = data["month_credits"]
        self.month_reset_at = data["month_reset_at"]
        self.max_cost_per_month = data["max_cost_per_month"]
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

        self.teamspeak = TeamspeakModel(data["teamspeak3_settings"]) \
            if data["teamspeak3_settings"] else None
        self.teamfortress = TeamFortressModel(data["teamfortress2_settings"]) \
            if data["teamfortress2_settings"] else None
        self.mumble = MumbleModel(data["mumble_settings"]) \
            if data["mumble_settings"] else None
        self.csgo = CsgoModel(data["csgo_settings"]) \
            if data["csgo_settings"] else None

        self._scheduled_commands = data["scheduled_commands"]

    def scheduled_commands(self) \
            -> typing.Generator[ScheduledCommandsModel, None, None]:
        """Lists scheduled commands.

        Yields
        ------
        ScheduledCommandsModel
            Holds data on scheduled commands.
        """

        for data in self._scheduled_commands:
            yield ScheduledCommandsModel(data)
