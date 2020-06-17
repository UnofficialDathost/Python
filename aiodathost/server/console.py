from ..wrapped_requests import AWR
from ..routes import ROUTES
from ..exceptions import InvalidMaxLines


class Console:
    def __init__(self, server_id):
        self.server_id = server_id

    async def get(self, max_lines: int = 1000):
        """
        Get the last line of backlong.

        max_lines: int
            Can range between 1 to 1000.
        """

        if type(max_lines) == int and max_lines <= 1000 and max_lines >= 1:
            data = await AWR(
                ROUTES.console_get.format(
                   self.server_id
                ),
                params={
                    "max_lines": max_lines,
                }
            ).get()

            return data["lines"]
        else:
            raise InvalidMaxLines()

    async def send(self, line: str):
        """
        Sends a command to the console.

        line: str
            Command to send to the console.
        """

        return await AWR(
            ROUTES.console_send.format(
                self.server_id,
                params={
                    "line": line,
                }
            )
        ).post()
