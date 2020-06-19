##### async aiodathost.client.server.backup.restore

**Functionality**

Restores backup to that server.


**Parameters**

None

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").backup(
        backup_name="..."
    ).restore()
```

___