## Install
Install git and run `pip install git+https://github.com/DistrictNineHost/aiodathost.git`

[Dathost's API documentation](https://dathost.net/api)

### Useful notes:
- The path is counted from the root node as seen in the file manager in the control panel, i.e. to write csgo/cfg/server.cfg the path would be cfg/server.cfg, if the path ends with / a directory will be created and the file parameter will be ignored.
- There is a upload limit of 100MB on dathost.net, our wrapper uses upload.dathost.net to upload files up to 500MB.
- Pathways should always end in a '/'.
- Sync function should be called before downloading files.
- Our API wrapper will return false if it fails, so check for that.
- Check Dathost's documentation for data returns, if it doesn't return any data our wrapper will just return True.
- Use await dathost.session.close() to close the session, example [here](/aiodathost/aiodathost.py#L199)
- Make sure to read the docstrings for help.

## Example
```python
from aiodathost.aiodathost import dathost

dathost = dathost(username = "contact@districtnine.host", password = "********", route = "https://dathost.net/api/0.1")

async def example():
    # Account Interactions

    # Returns list of domains on dathost.
    domains = await dathost.domains()
    print(domains)

    # Returns account infomation.
    account_details = await dathost.account()
    print(account_details)

    # Returns full list of details about all the game servers.
    all_servers_details = await dathost.details()
    print(all_servers_details)

    # Game Server Interactions

    # Starts given server id.
    await dathost.server.start(server_id)

    # Resets given server id.
    await dathost.server.reset(server_id)

    # Spawns new dathost server.
    # https://dathost.net/api#!/default/post_game_servers
    # e.g. server_details={"game": "csgo", etc}
    await dathost.server.create(server_details)

    # Stops given server.
    await dathost.server.stop(server_id)

    # Returns metricis saved by dathost about a game server.
    metrics = await dathost.server.metrics(server_id)
    print(metrics)

    # Clones a game server and returns infomation on it.
    cloning = await dathost.server.clone(server_id)
    print(cloning)

    # Deletes given server.
    await dathost.server.delete(server_id)

    # Generate a new random ftp password.
    await dathost.server.ftp_regenerate(server_id)

    # Returns details on a game server.
    details = await dathost.server.details(server_id)
    print(details)

    # Console Interactions

    # Sends a line to the console.
    await dathost.console.send(server_id, console_line)

    # Gets x amount of lines from the console from the game server.
    console = await dathost.console.pull(server_id, max_lines = 1)
    print(console)

    # File Interactions

    # Deletes file from given server.
    # Pathway should always end in a /.
    await dathost.files.delete(server_id, pathway, file_name)

    # Syncs files between given server.
    await dathost.files.sync(server_id)

    # Uploads file to game server.
    await dathost.files.upload(server_id, pathway, local_pathway, file_name, upload_route = "https://upload.dathost.net/api/0.1")

    # Unzips file on game server.
    await dathost.files.unzip(server_id, pathway, file_name)

    # Returns files on a game server.
    # Pathway should always end in a /.
    files = await dathost.files.list(server_id, pathway = "", hide_default_files = False, with_filesizes = False)
    print(files)

    # Downloads a file from the game server.
    # Use aiofiles to save it.
    downloaded_file = await dathost.files.download(server_id, pathway, file_name)

    # Make sure to close the session.
    # This should only be done once.
    await dathost.session.close()
```
