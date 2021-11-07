import unittest

from secrets import token_urlsafe

from .shared_vars import TEST_IMAGE_DIRETORY

from ..models.account import AccountModel
from ..models.server import ServerModel
from ..models.file import FileModel
from ..models.backup import BackupModel
from ..models.metrics import (
    MetricsModel,
    MapsModel,
    PlayerModel,
    PlayersOnlineGraphModel
)
from ..models.match import (
    MatchModel, TeamModel, MatchPlayerModel, MatchSeriesModel
)

from ..server.blocking.backup import BlockingBackup
from ..server.blocking.file import BlockingFile

from ..match.blocking import BlockingMatch, BlockingSeries

from ..server.blocking import ServerBlocking

from ..settings import (
    MatchMapSettings, ServerSettings, MatchSettings, MatchSeriesSettings
)

from .. import Blocking


class TestBlockingClient(unittest.TestCase):
    email: str
    password: str

    def setUp(self):
        self.client = Blocking(
            email=self.email,
            password=self.password,
            timeout=360
        )

    def tearDown(self):
        self.client.close()

    def test_blocking_account(self):
        account = self.client.account()

        self.assertTrue(isinstance(account, AccountModel))

    def test_blocking_domains(self):
        for domain in self.client.domains():
            self.assertTrue(type(domain) == str)

    def test_blocking_context(self):
        with Blocking(self.email, self.password) as client:
            client.account()

        with Blocking(self.email, self.password) as client:
            for domain in client.domains():
                pass

    def test_blocking_list_servers(self):
        for data, server in self.client.servers():
            self.assertIsInstance(data, ServerModel)
            self.assertIsInstance(server, ServerBlocking)

    def test_blocking_server_csgo(self):
        server_data, server = self.client.create_server(
            ServerSettings(
                name="Blocking CS: GO server",
                location="sydney",
            ).csgo(
                slots=5,
                game_token="",
                tickrate=128,
                rcon_password=token_urlsafe()
            )
        )

        self.assertIsInstance(server_data, ServerModel)
        self.assertIsInstance(server, ServerBlocking)

        self.assertIsInstance(server.get(), ServerModel)

        server.console_send("status")
        server.console_retrive()

        server.start()
        server.stop()
        server.reset()

        server.update(
            ServerSettings(
                name="Renamed Blocking CS: GO server",
                location="sydney"
            ).csgo(
                slots=7
            )
        )

        for data, f in server.files():
            self.assertIsInstance(data, FileModel)
            self.assertIsInstance(f, BlockingFile)

        for data, f in server.files(hide_default=True, file_sizes=True):
            self.assertIsInstance(data, FileModel)
            self.assertIsInstance(f, BlockingFile)

        for data, backup in server.backups():
            self.assertIsInstance(data, BackupModel)
            self.assertIsInstance(backup, BlockingBackup)

            backup.restore()

        metrics = server.metrics()
        self.assertIsInstance(metrics, MetricsModel)

        for map_ in metrics.maps():
            self.assertIsInstance(map_, MapsModel)

        for player in metrics.players_online():
            self.assertIsInstance(player, PlayerModel)

        for player in metrics.all_time_players():
            self.assertIsInstance(player, PlayerModel)

        for player in metrics.players_online_graph():
            self.assertIsInstance(player, PlayersOnlineGraphModel)

        server.ftp_reset()

        test_1_file = server.file("test.txt")
        self.assertIsNone(test_1_file.upload(b"hello world"))
        self.assertIsNone(test_1_file.move("cfg"))

        self.assertTrue(type(test_1_file.dowload()) == bytes)

        self.assertIsNone(test_1_file.delete())

        test_2_file = server.file("test.jpg")
        test_2_file.upload_file(TEST_IMAGE_DIRETORY)
        test_2_file.save(TEST_IMAGE_DIRETORY)

        self.assertIsNone(test_2_file.delete())

        _, duplicate = server.duplicate(sync=True)
        self.assertIsNone(duplicate.delete())

        match_data, match = server.create_match(
            MatchSettings(
            ).team_1(
                [
                    "[U:1:116962485]",
                    76561198017567105,
                    "STEAM_0:1:186064092"
                ]
            ).team_2(
                [
                    "[U:1:320762620]",
                    "STEAM_1:1:83437164",
                    76561198214871324
                ]
            )
        )

        self.assertIsInstance(match_data, MatchModel)
        self.assertIsInstance(match, BlockingMatch)

        self.assertIsInstance(match.get(), MatchModel)

        self.assertIsInstance(match_data.team_1, TeamModel)
        self.assertIsInstance(match_data.team_2, TeamModel)

        for player in match_data.players():
            self.assertIsInstance(player, MatchPlayerModel)

        series_data, series = server.create_series(
            MatchSeriesSettings(
                MatchSettings(
                ).team_1(
                    [
                        "[U:1:116962485]",
                        76561198017567105,
                        "STEAM_0:1:186064092"
                    ]
                ).team_2(
                    [
                        "[U:1:320762620]",
                        "STEAM_1:1:83437164",
                        76561198214871324
                    ]
                ),
                message_prefix="Greg"
            ).maps([
                MatchMapSettings(),
                MatchMapSettings(),
                MatchMapSettings()
            ])
        )

        self.assertIsInstance(series_data, MatchSeriesModel)
        self.assertIsInstance(series, BlockingSeries)

        for match in series_data.matches():
            self.assertIsInstance(match.team_1, TeamModel)
            self.assertIsInstance(match.team_2, TeamModel)

            for player in match.players():
                self.assertIsInstance(player, MatchPlayerModel)

        self.assertIsInstance(series.get(), MatchSeriesModel)

        self.assertIsNone(server.delete())

    def test_blocking_server_valheim(self):
        data, server = self.client.create_server(
            ServerSettings(
                name="Blocking valheim server",
                location="sydney"
            ).valheim(
                password=token_urlsafe(8),
                world_name="Poggers",
                plus=False,
                admins=[
                    "[U:1:116962485]",
                    76561198017567105,
                    "STEAM_0:1:186064092",
                    "76561198214871321"
                ]
            )
        )

        self.assertIsInstance(data, ServerModel)
        self.assertIsInstance(server, ServerBlocking)

        self.assertIsInstance(server.get(), ServerModel)

        self.assertIsNone(server.delete())

    def test_blocking_server_tf2(self):
        data, server = self.client.create_server(
            ServerSettings(
                name="Blocking TF2 server",
                location="sydney"
            ).tf2(
                slots=5,
                rcon_password=token_urlsafe()
            )
        )

        self.assertIsInstance(data, ServerModel)
        self.assertIsInstance(server, ServerBlocking)

        self.assertIsInstance(server.get(), ServerModel)

        self.assertIsNone(server.delete())

    def test_blocking_server_teamspeak(self):
        data, server = self.client.create_server(
            ServerSettings(
                name="Blocking TF2 server",
                location="sydney"
            ).teamspeak(
                slots=5,
            )
        )

        self.assertIsInstance(data, ServerModel)
        self.assertIsInstance(server, ServerBlocking)

        self.assertIsInstance(server.get(), ServerModel)

        self.assertIsNone(server.delete())
