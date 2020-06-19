# Index

___

##### async aiodathost.client.server.create

**Functionality**

Creates a server, responses with the data & sets the current
initialized object to the created server's ID.


**Parameters**

- kwargs

If the parameter includes a '.' replace it with '__'.

**Response**

ServerModel

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server().create(
        game="csgo",
        name="Awesome test server",
        csgo_settings__rcon="something secure"
    )
```

___

##### async aiodathost.client.server.reset

**Functionality**

Resets given server to default files.


**Parameters**

None

**Response**

ServerModel

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").reset()
```

___

##### async aiodathost.client.server.metrics

**Functionality**

Gets metrics about server.


**Parameters**

None

**Response**

MetricsModel

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    metrics = await DATHOST.server(server_id="...").metrics()
```

___

##### async aiodathost.client.server.ftp_reset

**Functionality**

Sets a new random FTP password for the server.


**Parameters**

None

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").ftp_reset()
```

___

##### async aiodathost.client.server.start

**Functionality**

Attempts to start given server.


**Parameters**

- allow_host_reassignment: bool
    - If true, the server may be moved to another host/port if the current host is unreachable.

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").start()
```

___

##### async aiodathost.client.server.stop

**Functionality**

Attempts to stop given server.


**Parameters**

None

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").stop()
```

___

##### async aiodathost.client.server.sync

**Functionality**

Ensures all files are synced.


**Parameters**

None

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").sync()
```

___

##### async aiodathost.client.server.files

**Functionality**

Lists files on the server.


**Parameters**

- pathway: str
    - Path to use as root, leave empty to get all files

- hide_default_files: bool
    - If true, only files added by the user will be shown, default is all files.

- with_filesizes: bool
    - If true, return filesizes with filenames

**Response**

- path
- File object.

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    async for path, file in DATHOST.server(server_id="...").files():
        print(path)
        await file.delete()
```

___

##### async aiodathost.client.server.backups

**Functionality**

Lists backups.


**Parameters**

None

**Response**

- BackupModel
- Backup object.

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    async for data, backup in DATHOST.server(server_id="...").backups():
        print(data.name)
        await backup.restore()
```

___

##### async aiodathost.client.server.duplicate

**Functionality**

Duplicates given server.


**Parameters**

None

**Response**

- ServerModel
- Server.

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    data, server = await DATHOST.server(server_id="...").duplicate()
    print(data.id)
    await server.start()
```

___

##### async aiodathost.client.server.delete

**Functionality**

Deletes current server.


**Parameters**

None

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").delete()
```

___

##### async aiodathost.client.server.get

**Functionality**

Gets details about the game server.


**Parameters**

None

**Response**

- ServerModel

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    data = await DATHOST.server(server_id="...").get()
    print(data.id)
```

___

##### aiodathost.client.server.console

**Parameters**

None

[Console documentation](/docs/console.md)

___

##### aiodathost.client.server.file

**Parameters**

- pathway: str
    - Pathway of file on dathost.

[File documentation](/docs/file.md)

___

##### aiodathost.client.server.backup

**Parameters**

- backup_name: str
    - Backup name.

[Backup documentation](/docs/backup.md)

___