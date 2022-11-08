import asyncio
import os
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from meross_iot.model.enums import OnlineStatus
from ...abstractions.filters.DevicesFilter import DevicesFilter
from ...abstractions.Device import Device
from ...abstractions.ToggledDevice import ToggledDevice


class ManagerUtils():

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

    async def GetDevices(self, devicesType: [str]) -> []:
        devices: [Device] = []
        
        await self.manager.async_device_discovery()

        for device in devicesType:
            discoveredDevices = self.manager.find_devices(device_type=device)

            await dev.async_update()

            if (len(discoveredDevices) > 0):
                for discoveredDevice in discoveredDevices:
                    devices.append(discoveredDevice)

        return devices

    async def ToggleDevice(self, toggledDevice: ToggledDevice) -> str:
        deviceId: str = None

        await self.manager.async_device_discovery()
        device = self.manager.find_devices(toggledDevice.deviceId)[0]
        await device.async_update()

        if (device != None):
            deviceId = device.uuid

            if (toggledDevice.enabled == True):
                await device.async_turn_on(channel=0)
            else:
                await device.async_turn_off(channel=0)

        return deviceId


class Manager(ManagerUtils):

    def __init__(self, user, passwd) -> None:
        super().__init__(user, passwd)

    async def StartManager(self):
        await super().StartClient()
        await super().StartManager()
        return super()
