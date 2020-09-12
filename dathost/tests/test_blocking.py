import unittest

from secrets import token_urlsafe

from ..models.account import AccountModel
from ..models.server import ServerModel
from ..models.file import FileModel
from ..models.backup import BackupModel
from ..models.metrics import MetricsModel, MapsModel, PlayerModel, \
    PlayersOnlineGraphModel

from ..server.blocking.backup import Backup
from ..server.blocking.file import BlockingFile

from ..server.blocking import ServerBlocking

from ..settings import ServerSettings

from .. import Blocking

from .shared_vars import EMAIL, PASSWORD, TEST_IMAGE_DIRETORY


class TestBlockingClient(unittest.TestCase):
    def setUp(self):
        self.client = Blocking(
            email=EMAIL,
            password=PASSWORD
        )

    def tearDown(self):
        self.client.close()

    def test_account(self):
        account = self.client.account()

        self.assertTrue(isinstance(account, AccountModel))

    def test_domains(self):
        for domain in self.client.domains():
            self.assertTrue(type(domain) == str)

    def test_context(self):
        with Blocking(EMAIL, PASSWORD) as client:
            client.account()

    def test_list_servers(self):
        for data, server in self.client.servers():
            self.assertIsInstance(data, ServerModel)
            self.assertIsInstance(server, ServerBlocking)

    def test_server_csgo(self):
        data, server = self.client.create_server(
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

        self.assertIsInstance(data, ServerModel)
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
            self.assertIsInstance(backup, Backup)

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

        self.assertIsNone(server.delete())

    def test_server_mumble(self):
        data, server = self.client.create_server(
            ServerSettings(
                name="Blocking Mumble server",
                location="sydney"
            ).mumble(
                slots=7,
                superuser_password=token_urlsafe()
            )
        )

        self.assertIsInstance(data, ServerModel)
        self.assertIsInstance(server, ServerBlocking)

        self.assertIsInstance(server.get(), ServerModel)

        self.assertIsNone(server.delete())

    def test_server_tf2(self):
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

    def test_server_teamspeak(self):
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
