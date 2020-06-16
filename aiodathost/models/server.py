class ConnectModels:
    def __init__(self, data):
        self.game = "{}:{}".format(
            data["ip"],
            data["ports"]["game"]
        )
        self.gotv = "{}:{}".format(
            data["ip"],
            data["ports"]["gotv"]
        )


class PortsModel:
    def __init__(self, data):
        self.game = data["ports"]["game"]
        self.gotv = data["ports"]["gotv"]


class MysqlModel:
    def __init__(self, data):
        self.enabled = data["enable_mysql"]
        self.username = data["mysql_username"]
        self.password = data["mysql_password"]


class CsgoModel:
    def __init__(self, data):
        csgo_settings = data["csgo_settings"]

        self.slots = csgo_settings["slots"]
        self.game_token = csgo_settings[
            "steam_game_server_login_token"
        ]
        self.rcon = csgo_settings["rcon"]
        self.password = csgo_settings["password"]
        self.maps_source = csgo_settings["maps_source"]
        self.mapgroup = csgo_settings["mapgroup"]
        self.mapgroup_start_map = csgo_settings["mapgroup_start_map"]
        self.workshop_id = csgo_settings["workshop_id"]
        self.workshop_start_map_id = csgo_settings["workshop_start_map_id"]
        self.workshop_authkey = csgo_settings["workshop_authkey"]
        self.autoload_configs = csgo_settings["autoload_configs"]
        self.sourcemod_admins = csgo_settings["sourcemod_admins"]
        self.sourcemod_plugins = csgo_settings["sourcemod_plugins"]
        self.enable_gotv = csgo_settings["enable_gotv"]
        self.enable_sourcemod = csgo_settings["enable_sourcemod"]
        self.enable_csay_plugin = csgo_settings["enable_csay_plugin"]
        self.game_mode = csgo_settings["game_mode"]
        self.tickrate = csgo_settings["tickrate"]
        self.pure_server = csgo_settings["pure_server"]
        self.insecure = csgo_settings["insecure"]
        self.disable_bots = csgo_settings["disable_bots"]


class MumbleModel:
    def __init__(self, data):
        mumble_settings = data["mumble_settings"]

        self.slots = mumble_settings["slots"]
        self.password = mumble_settings["password"]
        self.superuser_password = mumble_settings["superuser_password"]
        self.welcome_text = mumble_settings["welcome_text"]


class TF2Model:
    def __init__(self, data):
        tf2_settings = data["teamfortress2_settings"]

        self.slots = tf2_settings["slots"]
        self.rcon = tf2_settings["rcon"]
        self.password = tf2_settings["password"]
        self.sourcemod_admins = tf2_settings["sourcemod_admins"]
        self.enable_gotv = tf2_settings["enable_gotv"]
        self.enable_sourcemod = tf2_settings["enable_sourcemod"]
        self.insecure = tf2_settings["insecure"]


class TeamSpeak3Model:
    def __init__(self, data):
        ts3_settings = data["teamspeak3_settings"]

        self.slots = ts3_settings["slots"]
        self.admin_token = ts3_settings["ts_admin_token"]


class ServerModel:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.user = data["user_data"]
        self.game = data["game"]
        self.location = data["location"]
        self.players_online = data["players_online"]
        self.status = data["status"]
        self.booting = data["booting"]
        self.server_error = data["server_error"]
        self.ip = data["ip"]
        self.on = data["on"]
        self.ports = PortsModel(data)
        self.connect = ConnectModels(data)
        self.confirmed = data["confirmed"]
        self.cost_per_hour = data["cost_per_hour"]
        self.max_cost_per_hour = data["max_cost_per_hour"]
        self.month_credits = data["month_credits"]
        self.month_reset_at = data["month_reset_at"]
        self.max_cost_per_month = data["max_cost_per_month"]
        self.mysql = MysqlModel(data)
        self.autostop = data["autostop"]
        self.autostop_minutes = data["autostop_minutes"]
        self.ftp_password = data["ftp_password"]
        self.disk_usage_bytes = data["disk_usage_bytes"]
        self.default_file_locations = data["default_file_locations"]
        self.custom_domain = data["custom_domain"]
        self.scheduled_commands = data["scheduled_commands"]
        self.added_voice_server = data["added_voice_server"]
        self.duplicate_source_server = data["duplicate_source_server"]
        self.csgo = CsgoModel(data)
        self.mumble = MumbleModel(data)
        self.tf2 = TF2Model(data)
        self.teamspeak3 = TeamSpeak3Model(data)
