# Index

### Exceptions
___

##### aiodathost.exceptions.InvalidAuthorization

**Parameters**

None

**Functionality**

Raised when authorization is invalid.

**Response**

None

**Raises**

- InvalidAuthorization

**Example**

```python
import aiodathost

try:
    raise aiodathost.exceptions.InvalidAuthorization()
except aiodathost.exceptions.InvalidAuthorization:
    pass
```

___

##### aiodathost.exceptions.BadRequest

**Parameters**

None

**Functionality**

Raised when a bad request was sent.

**Response**

None

**Raises**

- BadRequest

**Example**

```python
import aiodathost

try:
    raise aiodathost.exceptions.BadRequest()
except aiodathost.exceptions.BadRequest:
    pass
```

___

##### aiodathost.exceptions.NotFound

**Parameters**

None

**Functionality**

Raised when a ID was not found.

**Response**

None

**Raises**

- NotFound

**Example**

```python
import aiodathost

try:
    raise aiodathost.exceptions.NotFound()
except aiodathost.exceptions.NotFound:
    pass
```

___

##### aiodathost.exceptions.AboveDiskQuota

**Parameters**

None

**Functionality**

Raised when your disk quota of 30GB per server (excluding base installation) has been exceeded.

**Response**

None

**Raises**

- AboveDiskQuota

**Example**

```python
import aiodathost

try:
    raise aiodathost.exceptions.AboveDiskQuota()
except aiodathost.exceptions.AboveDiskQuota:
    pass
```

___

##### aiodathost.exceptions.InvalidMaxLines

**Parameters**

None

**Functionality**

Raised when lines are above 1 & 1,000.

**Response**

None

**Raises**

- InvalidMaxLines

**Example**

```python
import aiodathost

try:
    raise aiodathost.exceptions.InvalidMaxLines()
except aiodathost.exceptions.InvalidMaxLines:
    pass
```

___

##### aiodathost.exceptions.RequestTimeout

**Parameters**

None

**Functionality**

Raised when Dathost timed out our request.

**Response**

None

**Raises**

- RequestTimeout

**Example**

```python
import aiodathost

try:
    raise aiodathost.exceptions.RequestTimeout()
except aiodathost.exceptions.RequestTimeout:
    pass
```

___

##### aiodathost.exceptions.InternalError

**Parameters**

None

**Functionality**

Raised when an internal error occurred on dathost's end.

**Response**

None

**Raises**

- InternalError

**Example**

```python
import aiodathost

try:
    raise aiodathost.exceptions.InternalError()
except aiodathost.exceptions.InternalError:
    pass
```

___

##### aiodathost.exceptions.UndefinedError

**Parameters**

None

**Functionality**

Raised when an error aiodathost can't understand was passed.
**Response**

None

**Raises**

- UndefinedError

**Example**

```python
import aiodathost

try:
    raise aiodathost.exceptions.UndefinedError()
except aiodathost.exceptions.UndefinedError:
    pass
```

___