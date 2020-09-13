Intro
=====
This wrapper has both asynchronous & synchronous support, this intro will cover the basic of both.
Lucily for you the API for asynchronous (awaiting) & synchronous (blocking) is identical.

Non-context managers
--------------------

**Awaiting client**

.. code-block:: python

    import dathost

    client = dathost.Awaiting(
        email="wardpearce@protonmail.com",
        password="..."
    )

    # A client should always be closed after being used!
    await client.close()


**Blocking client**

.. code-block:: python

    import dathost

    client = dathost.Blocking(
        email="wardpearce@protonmail.com",
        password="..."
    )

    # A client should always be closed after being used!
    client.close()

Context managers
----------------
**Blocking**

.. code-block:: python

    import dathost

    with dathost.Blocking(EMAIL, PASSWORD) as client:
        pass

**Awaiting**

.. code-block:: python

    import dathost

    async with dathost.Awaiting(EMAIL, PASSWORD) as client:
        pass
