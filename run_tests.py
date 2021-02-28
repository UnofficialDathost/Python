import unittest
import argparse
import sys

from dathost.tests.test_blocking import TestBlockingClient
from dathost.tests.test_awaiting import TestAwaitingClient


cli = argparse.ArgumentParser()

cli.add_argument("--email", type=str, default="wpearce6@gmail.com")
cli.add_argument("--password", type=str, default="hCG6mdpFGXKxQLnUh55ztrXMnweBZyD99Eh")

args = vars(cli.parse_args())


if __name__ == "__main__":
    TestBlockingClient.email = args["email"]
    TestBlockingClient.password = args["password"]

    TestAwaitingClient.email = args["email"]
    TestAwaitingClient.password = args["password"]

    unittest.main(argv=[sys.argv[0]])
