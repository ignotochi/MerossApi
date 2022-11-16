import asyncio
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient


class Manager():

    __manager: MerossManager = None
    __client: MerossHttpClient = None

    @classmethod
    def __init__(cls, user: str, passwd: str) -> None:
        asyncio.run(cls.Start(user, passwd))

    @classmethod
    async def Start(cls, user: str, passwd: str) -> None:

        newIstanceNeeded = isinstance(cls.__manager, MerossManager) == False and isinstance(cls.__client, MerossHttpClient) == False

        if (newIstanceNeeded):
            await cls.__StartClient(user, passwd)
            await cls.__StartManager()

    @classmethod
    async def __StartClient(cls, user: str, passwd: str) -> None:
        cls.__client = await MerossHttpClient.async_from_user_password(email=user, password=passwd)

    @classmethod
    async def __StartManager(cls) -> None:
        cls.__manager = MerossManager(http_client=cls.__client)
        await cls.__manager.async_init()

    @classmethod
    def GetClient(cls) -> MerossHttpClient:
        return cls.__client

    @classmethod
    def GetManager(cls) -> MerossManager:
        return cls.__manager

    @classmethod
    def __del__(cls):
       del cls


