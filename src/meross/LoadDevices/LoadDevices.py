import asyncio
import os
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from ...abstractions.IDevices import IDevices
from ...costatnts import *

class Devices(IDevices):

    async def LoadMerossDevices(user, passwd):
        # Setup the HTTP client API from user-password
        http_api_client = await MerossHttpClient.async_from_user_password(email=user, password=passwd)

        # Setup and start the device manager
        manager = MerossManager(http_client=http_api_client)
        await manager.async_init()

        # Retrieve all the MSS310 devices that are registered on this account
        await manager.async_device_discovery()
        plugs = manager.find_devices(device_type = MSS_710)

        if len(plugs) < 1:
            print("No MSS310 plugs found...")
        else:        
            return plugs

        manager.close()
        await http_api_client.async_logout()

    # if __name__ == '__main__':
    #     # Windows and python 3.8 requires to set up a specific event_loop_policy.
    #     #  On Linux and MacOSX this is not necessary.
    #     if os.name == 'nt':
    #         asyncio.set_event_loop_policy(
    #             asyncio.WindowsSelectorEventLoopPolicy())
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(main())
    #     loop.close()
