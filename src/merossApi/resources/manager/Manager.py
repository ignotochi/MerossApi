import asyncio
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from merossApi.core.Singleton import Singleton
 
@Singleton.New
class Manager(object):
    
    @classmethod
    def __init__(cls, user: str, passwd: str) -> None:
        cls.manager: MerossManager = None
        cls.client: MerossHttpClient = None
        
        asyncio.run(cls.Start(user, passwd))
            
    @classmethod
    async def Start(cls, user: str, passwd: str) -> None:
        try:
            newIstanceNeeded = isinstance(cls.manager, MerossManager) == False and isinstance(cls.client, MerossHttpClient) == False
           
            if (newIstanceNeeded):
                cls.client = await cls.__StartClient(user, passwd)
                cls.manager = await cls.__StartManager(cls.client)
            else:
                eventLoop = asyncio.get_event_loop()
                cls.manager._loop = eventLoop

        except Exception as exception:
            raise Exception(exception.args[0])

    @classmethod
    async def __StartClient(cls, user: str, passwd: str) -> MerossHttpClient:
        return await MerossHttpClient.async_from_user_password(email=user, password=passwd)

    @classmethod
    async def __StartManager(cls, client: MerossHttpClient) -> MerossManager:
        manager = MerossManager(http_client=client, auto_reconnect= True, mqtt_skip_cert_validation=True)
        await manager.async_init()
        return manager

    @classmethod
    def Reset(cls) -> None:
        Singleton.Clean(cls)
