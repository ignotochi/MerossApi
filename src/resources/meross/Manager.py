import asyncio
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross_iot.controller.device import BaseDevice
from ...abstractions.DeviceType import DeviceType


class Manager(object):

    manager: MerossManager = None
    client: MerossHttpClient = None

    @classmethod
    def __init__(cls, user: str, passwd: str) -> None:
        asyncio.run(cls.Start(user, passwd))

    @classmethod
    async def Start(cls, user: str, passwd: str) -> None:

        newIstanceNeeded = isinstance(cls.manager, MerossManager) == False and isinstance(cls.client, MerossHttpClient) == False

        if (newIstanceNeeded):
            await cls.__StartClient(user, passwd)
            await cls.__StartManager()

        await cls.Discover()

        discoveredDevices = cls.Find()

        if (discoveredDevices and len(discoveredDevices) > 0):
            for discoveredDevice in discoveredDevices:
                await cls.Update(discoveredDevice)

    @classmethod
    async def __StartClient(cls, user: str, passwd: str) -> None:
        cls.client = await MerossHttpClient.async_from_user_password(email=user, password=passwd)

    @classmethod
    async def __StartManager(cls) -> None:
        cls.manager = MerossManager(http_client=cls.client)
        await cls.manager.async_init()

    @classmethod
    def Find(cls, devicesType: [DeviceType] = None) -> [BaseDevice]:
        discoverdDevices = cls.manager.find_devices(device_type=devicesType)
        return discoverdDevices

    @classmethod
    async def Discover(cls) -> None:
        await cls.manager.async_device_discovery()

    @classmethod
    async def Update(cls, device: BaseDevice):
        await device.async_update()
