import asyncio
import os
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from ..abstractions.IDevices import IDeviceRepository
from ..costatnts import *


class DeviceRepository(IDeviceRepository):

    async def LoadMerossDevices(user, passwd):
        # Setup the HTTP client API from user-password
        http_api_client = await MerossHttpClient.async_from_user_password(email=user, password=passwd)

        # Setup and start the device manager
        manager = MerossManager(http_client=http_api_client)
        await manager.async_init()

        # Retrieve all the MSS310 devices that are registered on this account
        await manager.async_device_discovery()
        plugs = manager.find_devices(device_type=MSS_710)

        if len(plugs) < 1:
            print("No MSS310 plugs found...")
        else:
            return plugs

        manager.close()
        await http_api_client.async_logout()

    if __name__ == '__main__' and os.name == 'nt':

        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()

    async def ToggleMerossDevice(user, passwd):
        # Setup the HTTP client API from user-password
        http_api_client = await MerossHttpClient.async_from_user_password(email=EMAIL, password=PASSWORD)

        # Setup and start the device manager
        manager = MerossManager(http_client=http_api_client)
        await manager.async_init()

        # Retrieve all the MSS310 devices that are registered on this account
        await manager.async_device_discovery()
        plugs = manager.find_devices(device_type=MSS_710)

        if len(plugs) < 1:
            print("No MSS310 plugs found...")
        else:
            # Turn it on channel 0
            # Note that channel argument is optional for MSS310 as they only have one channel
            dev = plugs[0]

            # Update device status: this is needed only the very first time we play with this device (or if the
            #  connection goes down)
            await dev.async_update()

            print(f"Turning on {dev.name}...")
            await dev.async_turn_on(channel=0)
            print("Waiting a bit before turing it off")
            await asyncio.sleep(5)
            print(f"Turing off {dev.name}")
            await dev.async_turn_off(channel=0)

        # Close the manager and logout from http_api
        manager.close()
        await http_api_client.async_logout()

    if __name__ == '__main__':
        if os.name == 'nt':
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
