import unittest

from ..models.account import AccountModel
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
        domains = self.client.domains()

        self.assertTrue(type(domains) == list)

    def test_context(self):
        with Blocking(EMAIL, PASSWORD) as client:
            client.account()
