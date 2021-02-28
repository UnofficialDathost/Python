import unittest
import argparse
import sys

from dathost.tests.test_blocking import TestBlockingClient
from dathost.tests.test_awaiting import TestAwaitingClient


cli = argparse.ArgumentParser()

cli.add_argument("--email", type=str, default="")
cli.add_argument("--pw", type=str, default="")

args = vars(cli.parse_args())


if __name__ == "__main__":
    TestBlockingClient.email = args["email"]
    TestBlockingClient.password = args["pw"]

    TestAwaitingClient.email = args["email"]
    TestAwaitingClient.password = args["pw"]

    unittest.main(argv=[sys.argv[0]])
