##### Version 5 is NOT backwards compatibility with version 4.

# Index
- [About](#about)
- [Install](#install)
- [Example](#example)
- [Dathost's API documentation](https://dathost.net/api)

# About
``aiodathost`` is a asynchronous wrapper what makes using Dathost's API easy. Version 5.0.0 is considered a rewrite and as a result everything below that version is incompatible.

# Install
- Pypi: `pip3 install aiodathost`
- Git: `pip3 install git+https://github.com/WardPearce/aiodathost.git`

# Example

```python
import aiodathost
import asyncio

dathost = aiodathost.client(
    email="...",
    password="..."
)

async def example():
    try:
        await dathost.account()
    except aiodathost.exceptions.InvalidAuthorization:
        print("Invalid login details")
    else:
        async for data, server in dathost.servers():
            print(data.id)
            await server.start()

    await dathost.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
```