## Install
Install git and run `pip install git+https://github.com/WardPearce/aiodathost.git`

[Dathost's API documentation](https://dathost.net/api)

## Example
```python
from aiodathost import dathost

dathost = dathost(username="contact@districtnine.host", password="********")

async def example():
    # Starting server.
    await dathost.start("server-id")

    # Stopping server.
    await dathost.stop("server-id")

    # Sends a line to the server console.
    await dathost.send_console("server-id", "say hello world")

    # Deletes server.
    await dathost.delete("server-id")

    # Deletes file from server.
    # The path is counted from the root node as seen in the file manager in the control panel, i.e. to delete csgo/cfg/server.cfg the path 
    # would be cfg/server.cfg.
    await dathost.delete_file("server-id", "path-to-file")

    # Syncs files from cache.
    await dathost.sync("server-id")

    # FTP password regenerate.
    await dathost.ftp_regenerate("server-id")

    # Server details.
    await dathost.game_details("server-id")

    # Download file.
    # The path is counted from the root node as seen in the file manager in the control panel, i.e. to delete csgo/cfg/server.cfg the path 
    # would be cfg/server.cfg.
    await dathost.download("server-id", "path-to-file")

    # Returns account info.
    await dathost.account()

    # Returns details on every game server.
    await dathost.details()

    # Returns metricis saved by dathost about a game server.
    await dathost.metrics("server-id")

    # Clones a game server and returns infomation on it.
    await dathost.clone("server-id")
```