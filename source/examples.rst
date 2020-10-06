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


Creating a match
~~~~~~~~~~~~~~~~

.. code-block:: python

    from dathost.settings import MatchSettings

    data, match = server.create_match(
        MatchSettings(
            connection_time=60,
        ).team_1(
            [
                "[U:1:116962485]",
                76561198017567105,
                "STEAM_0:1:186064092"
            ]
        ).team_2(
            [
                "[U:1:320762620]",
                "STEAM_0:1:83437164",
                76561198214871324
            ]
        ).spectators(
            [
                "[U:1:320762620]",
                "STEAM_0:1:83437164",
                76561198214871324
            ]
        )
    )

    # Don't worry about steam IDs, the wrapper
    # ensures they're all converted correctly.
