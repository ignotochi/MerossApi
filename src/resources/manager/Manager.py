import asyncio
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross_iot.controller.device import BaseDevice
from ...abstractions.DeviceModel import DeviceModel
from ...core.Singleton import Singleton
 
@Singleton
class Manager(object):

    # manager: MerossManager = None
    # client: MerossHttpClient = None

    @classmethod
    def __init__(cls, user: str, passwd: str) -> None:
        cls.manager = MerossManager
        cls.client = MerossHttpClient
        
        asyncio.run(cls.Start(user, passwd))

    @classmethod
    async def Start(cls, user: str, passwd: str) -> None:

        newIstanceNeeded = isinstance(cls.manager, MerossManager) == False and isinstance(cls.client, MerossHttpClient) == False

        if (newIstanceNeeded):
            try:
                await cls.__StartClient(user, passwd)
                await cls.__StartManager()
                await cls.manager.async_device_discovery()
               
                discoveredDevices = cls.manager.find_devices()
                
                if (discoveredDevices and len(discoveredDevices) > 0):
                    for discoveredDevice in discoveredDevices:
                        await discoveredDevice.async_update()
                    
            except Exception as exception:
                raise Exception(exception.args[0])

    @classmethod
    async def __StartClient(cls, user: str, passwd: str) -> None:
        cls.client = await cls.client.async_from_user_password(email=user, password=passwd)

    @classmethod
    async def __StartManager(cls) -> None:
        cls.manager = cls.manager(http_client=cls.client)
        await cls.manager.async_init()

    @classmethod
    def Reset(cls) -> None:
        cls.manager = None
        cls.client = None
