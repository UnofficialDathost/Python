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
