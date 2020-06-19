# Index
- [aiodathost.client](#aiodathostclient)
- [aiodathost.client.close](#async-aiodathostclientclose)
- [aiodathost.client.account](#async-aiodathostclientaccount)
- [aiodathost.client.domains](#async-aiodathostclientdomains)
- [aiodathost.client.servers](#async-aiodathostclientservers)
- [aiodathost.client.server](#aiodathostclientserver)

### Client
___

##### aiodathost.client

**Functionality**

Used to communicate to Dathost's API.


**Parameters**

- email: str
    - Dathost account email address.
- password: str
    - Dathost password.
- session: aiohttp.ClientSession
    - Optionally pass your own aiohttp.ClientSession.
- chunk_size: int
    - How many chunks should we read each loop.

**Response**

None

**Raises**

None

**Example**

```python
import aiodathost

# Rest of the examples will assume the client
# is stored under a variable called B2.
DATHOST = aiodathost.client(email="...", password="...")
```

___

##### async aiodathost.client.close

**Functionality**

Closes all sessions.


**Parameters**

None

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def shutdown():
    await DATHOST.close()
```

___

##### async aiodathost.client.account

**Functionality**

Gets details about account.


**Parameters**

None

**Response**

AccountModel

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    async for data in DATHOST.account():
        pass
```

___

##### async aiodathost.client.domains

**Functionality**

Gets all domains.


**Parameters**

None

**Response**

Domains

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    async for data in DATHOST.domains():
        # Data would just be a string what represents the domain.
        print(data)
```

___

##### async aiodathost.client.servers

**Functionality**

Lists all non-deleted servers.


**Parameters**

None

**Response**

- ServerModel
- Server

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    async for data, server in DATHOST.servers():
        print(data.id)
        await server.start()
```

___

##### aiodathost.client.server

**Parameters**

- server_id: str
    - Server ID.


**Notes**

Leave blank if creating a server

[Server documentation](/docs/server.md)

___