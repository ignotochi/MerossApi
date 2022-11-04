import asyncio
import os
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from meross_iot.model.enums import OnlineStatus
from ...abstractions.DevicesFilter import DevicesFilter


class ConnectionManager():

    manager: MerossManager
    client: MerossHttpClient

    user: str
    passwd: str

    def __init__(self, user, passwd) -> None:
        self.user = user
        self.passwd = passwd

    async def StartClient(self) -> None:
        self.client = await MerossHttpClient.async_from_user_password(email=self.user, password=self.passwd)

    async def StartManager(self) -> None:
        self.manager = MerossManager(http_client=self.client)
        await self.manager.async_init()

    async def StopManagerAndLogOut(self) -> None:
        self.manager.close()
        await self.client.async_logout()

        # if __name__ == 'src.resource.meross.connection' and os.name == 'nt':
        #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        #     loop = asyncio.get_event_loop()
        #     loop.run_until_complete(main())
        #     loop.close()

    async def GetDevices(self, filters: DevicesFilter) -> []:
        devices = []
        await self.manager.async_device_discovery()

        for device in filters.devices:
            discoveredDevices = self.manager.find_devices(device_type=device)

            if (len(discoveredDevices) > 0):
                for discoveredDevice in discoveredDevices:
                    devices.append(discoveredDevice)

        return devices


class Manager(ConnectionManager):

    def __init__(self, user, passwd) -> None:
        super().__init__(user, passwd)

    async def StartManager(self):
        await super().StartClient()
        await super().StartManager()
        return super()
