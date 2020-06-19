import aiodathost
import asyncio
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

dathost = aiodathost.client(
    email="",
    password=""
)


async def test():
    try:
        await dathost.account()
    except aiodathost.exceptions.InvalidAuthorization:
        print("Invalid login details")
    else:
        target_server = None

        async for _, server in dathost.servers():
            target_server = server

        if target_server:
            print("Attempting to start {}".format(target_server.server_id))

            try:
                await target_server.start()
            except Exception:
                print("Failed to start")
            else:
                print("Started")

            print("Attempting to stop {}".format(target_server.server_id))

            try:
                await target_server.stop()
            except Exception:
                print("Failed to stop")
            else:
                print("Stopped")

            print("Listing backups")

            async for data, _ in target_server.backups():
                print(data.name)
                print(data.timestamp)

            print("Backups listed.")

            await target_server.get()

            file = target_server.file("test.bin")

            print("Attempting to upload some data.")
            await file.upload(
                data=b"foobar"
            )
            print("File uploaded.")

            # Ensuring the given file is updated in the cache.
            await target_server.sync()

            print("Looping over uploaded data")
            async for data in file.download_iterate():
                print(data)

            print("Finished looping")

            print("Attempting to save file locally.")
            await file.save(
                local_pathway=os.path.join(
                    CURRENT_DIR,
                    "test.bin"
                )
            )
            print("Saved locally.")
        else:
            print("Please create a server before starting the test.")

    await dathost.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
