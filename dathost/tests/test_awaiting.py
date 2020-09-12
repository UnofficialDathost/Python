import asynctest

from secrets import token_urlsafe

from ..models.account import AccountModel
from ..models.server import ServerModel
from ..models.file import FileModel
from ..models.backup import BackupModel

from ..server.awaiting.backup import Backup

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

    async def test_list_servers(self):
        async for data, server in self.client.servers():
            self.assertIsInstance(data, ServerModel)
            self.assertIsInstance(server, ServerAwaiting)

    async def test_server_csgo(self):
        data, server = await self.client.create_server(
            ServerSettings(
                name="Awaiting CS: GO server",
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

        self.assertIsInstance(await server.get(), ServerModel)

        await server.console_send("status")
        await server.console_retrive()

        await server.start()
        await server.stop()
        await server.reset()

        await server.update(
            ServerSettings(
                name="Renamed Awaiting CS: GO server",
                location="sydney"
            ).csgo(
                slots=7
            )
        )

        async for data in server.files():
            self.assertIsInstance(data, FileModel)

        async for data in server.files(hide_default=True, file_sizes=True):
            self.assertIsInstance(data, FileModel)

        async for data, backup in server.backups():
            self.assertIsInstance(data, BackupModel)
            self.assertIsInstance(backup, Backup)

            await backup.restore()

        await server.ftp_reset()

        _, duplicate = await server.duplicate(sync=True)
        self.assertIsNone(await duplicate.delete())

        self.assertIsNone(await server.delete())

    async def test_server_mumble(self):
        data, server = await self.client.create_server(
            ServerSettings(
                name="Blocking Mumble server",
                location="sydney"
            ).mumble(
                slots=7,
                superuser_password=token_urlsafe()
            )
        )

        self.assertIsInstance(data, ServerModel)
        self.assertIsInstance(server, ServerAwaiting)

        self.assertIsInstance(await server.get(), ServerModel)

        self.assertIsNone(await server.delete())

    async def test_server_tf2(self):
        data, server = await self.client.create_server(
            ServerSettings(
                name="Awaiting TF2 server",
                location="sydney"
            ).tf2(
                slots=5,
                rcon_password=token_urlsafe()
            )
        )

        self.assertIsInstance(data, ServerModel)
        self.assertIsInstance(server, ServerAwaiting)

        self.assertIsInstance(await server.get(), ServerModel)

        await server.update(
            ServerSettings(
                name="Renamed Awaiting CS: GO server",
                location="sydney"
            ).csgo(
                slots=7
            )
        )

        self.assertIsNone(await server.delete())

    async def test_server_teamspeak(self):
        data, server = await self.client.create_server(
            ServerSettings(
                name="Blocking TF2 server",
                location="sydney"
            ).teamspeak(
                slots=5,
            )
        )

        self.assertIsInstance(data, ServerModel)
        self.assertIsInstance(server, ServerAwaiting)

        self.assertIsInstance(await server.get(), ServerModel)

        self.assertIsNone(await server.delete())
