import asynctest

from secrets import token_urlsafe

from ..models.account import AccountModel
from ..models.server import ServerModel

from ..server.awaiting import ServerAwaiting

from .. import Awaiting

from ..settings import ServerSettings

from .shared_vars import EMAIL, PASSWORD


class TestAwaitingClient(asynctest.TestCase):
    use_default_loop = True

    async def setUp(self):
        self.client = Awaiting(
            email=EMAIL,
            password=PASSWORD
        )

    async def tearDown(self):
        await self.client.close()

    async def test_account(self):
        account = await self.client.account()

        self.assertTrue(isinstance(account, AccountModel))

    async def test_domains(self):
        async for domain in self.client.domains():
            self.assertTrue(type(domain) == str)

    async def test_context(self):
        async with Awaiting(EMAIL, PASSWORD) as client:
            await client.account()

    async def test_create_server(self):
        data, server = await self.client.create_server(
            ServerSettings(
                name="Awaiting test server",
                location="sydney",
            ).csgo(
                slots=5,
                game_token="",
                tickrate=128,
                rcon_password=token_urlsafe()
            )
        )

        self.assertIsInstance(data, ServerModel)
        self.assertIsInstance(server, ServerAwaiting)

        self.assertIsNone(await server.delete())
