import asynctest

from ..models.account import AccountModel
from .. import Awaiting

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
        domains = await self.client.domains()

        self.assertTrue(type(domains) == list)

    async def test_context(self):
        async with Awaiting(EMAIL, PASSWORD) as client:
            await client.account()
