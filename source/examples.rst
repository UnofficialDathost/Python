Examples
========
Here are some simple examples on how to use this wrapper.
This is written using the blocking wrapper, but still applies to the awaiting wrapper.

Assume that "client" has been initialized.


Creating a server
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from dathost.settings import ServerSettings

    data, server = client.create_server(
        ServerSettings(
            name="CS: GO server",
            location="sydney",
        ).csgo(
            slots=5,
            game_token="",
            tickrate=128,
            rcon_password=""
        )
    )

    server.start()
    print(data.slots)
