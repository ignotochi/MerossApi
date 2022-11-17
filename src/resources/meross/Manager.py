import asyncio
import os
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient

class Manager():

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
   
    @classmethod
    async def __StartClient(cls, user: str, passwd: str) -> None:
        cls.client = await MerossHttpClient.async_from_user_password(email=user, password=passwd)

    @classmethod
    async def __StartManager(cls) -> None:
        cls.manager = MerossManager(http_client=cls.client)
        await cls.manager.async_init()

    # def __del__(self):
    #    pass


