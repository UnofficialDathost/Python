# Index
- [aiodathost.client.server.console.get](#async-aiodathostclientserverconsoleget)
- [aiodathost.client.server.console.send](#async-aiodathostclientserverconsolesend)
___

##### async aiodathost.client.server.console.get

**Functionality**

Get the last line of backlong.


**Parameters**

- max_lines: int
    - Can range between 1 to 1000.

**Response**

Lines from the console.

**Raises**

- Any request related exceptions.
- InvalidMaxLines.

**Example**

```python
async def example():
    lines = await DATHOST.server(server_id="...").console.get()
```

___

##### async aiodathost.client.server.console.send

**Functionality**

Sends a command to the console.


**Parameters**

- line: str
    - Command to send to the console.

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").console.send(
        line="sm plugins list"
    )
```

___
