import unittest

from secrets import token_urlsafe

from ..models.account import AccountModel
from ..models.server import ServerModel

from ..server.blocking import ServerBlocking

from ..settings import ServerSettings

from .. import Blocking

from .shared_vars import EMAIL, PASSWORD


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

    def test_create_server(self):
        data, server = self.client.create_server(
            ServerSettings(
                name="Dathost test server",
                location="sydney",
            ).csgo(
                slots=5,
                game_token="",
                tickrate=128,
                rcon_password=token_urlsafe()
            )
        )

        self.assertTrue(isinstance(data, ServerModel))
        self.assertTrue(isinstance(server, ServerBlocking))
