##### Version 4 is NOT backwards compatibility with version 3.

## Install
Install git and run `pip3 install git+https://github.com/WardPearce/aiodathost.git`

[Dathost's API documentation](https://dathost.net/api)

## Index
- [API](#API)
- [Example](#example)

### API
#### aiodathost.client(...).server(server_id=None)
    - get(self)
    - start(self)
    - reset(self)
    - stop(self)
    - send_command(self, command)
    - console(self, max_lines:int =1)
    - create(self, parameters: dict)
    - delete(self)
    - ftp_regenerate(self)
    - clone(self)
    - metrics(self)
#### aiodathost.client(...).server(server_id=None).files(pathway="", force_sync=False)
    - sync(self)
    - list(self, hide_default_files=False, with_filesizes=False)
    - download(self)
    - delete(self)
    - unzip(self)
    - upload(self, data: bytes)
#### aiodathost.client(...)
    - account(self)
    - domains(self)

### Example
```python
import aiodathost
import asyncio

async def example():
    # Pass your own aiohttp session if you don't want to create a new one.
    client = aiodathost.client(username="*******", password="*******", session=None)

    print(await client.server(server_id="").files().list())

    await client.session.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
```
