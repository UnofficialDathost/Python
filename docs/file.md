# Index

___

##### async aiodathost.client.server.file.unzip

**Functionality**

Unzips given file.


**Parameters**

- destination: str
    - Pathway to move the zip file content to.

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").file(
        pathway="cfg/foobar.zip"
    ).unzip(
        destination="cfg/something"
    )
```

___

##### async aiodathost.client.server.file.delete

**Functionality**

Deletes the given file or folder.


**Parameters**

None

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").file(
        pathway="cfg/foobar.zip"
    ).delete()
```

___

##### async aiodathost.client.server.file.download

**Functionality**

Downloads the file into memory.


**Parameters**

- as_text: bool
    - If true, files up to 100kB will be returned as text/plain and bigger files will return an error.

**Response**

Bytes

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    data = await DATHOST.server(server_id="...").file(
        pathway="cfg/foobar.zip"
    ).download()
```

___

##### async aiodathost.client.server.file.download_iterate

**Functionality**

Iterates over downloading file.


**Parameters**

- as_text: bool
    - If true, files up to 100kB will be returned as text/plain and bigger files will return an error.

**Response**

Bytes

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    async for data in await DATHOST.server(server_id="...").file(pathway="cfg/foobar.zip").download_iterate():
        print(data)
```

___

##### async aiodathost.client.server.file.save

**Functionality**

Saves file to local pathway.


**Parameters**

- local_pathway: str
    - Local pathway.

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").file(
        pathway="cfg/foobar.zip"
    ).save(
        local_pathway="wow/thats/cool/foobar.zip"
    )
```

___

##### async aiodathost.client.server.file.upload

**Functionality**

Uploads given data onto the given pathway.


**Parameters**

- data: bytes
    - Data to upload.

**Response**

None

**Raises**

Any request related exceptions.

**Notes**

If no bytes passed just creates the file/directory.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").file(
        pathway="cfg/foo.bin"
    ).upload(
        data=b"bar"
    )
```

___

##### async aiodathost.client.server.file.move

**Functionality**

Moves file to given destination.


**Parameters**

- destination: str
    - Pathway to move the file to.

**Response**

None

**Raises**

Any request related exceptions.

**Example**

```python
async def example():
    await DATHOST.server(server_id="...").file(
        pathway="cfg/foo.bin"
    ).move(
        destination="cfg/zips"
    )
```

___