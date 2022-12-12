import asyncio
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross.abstractions.manager.IManager import IManager


class Manager(IManager):

    def manager(self, value):
        self.manager = value

    def client(self, value):
        self.client = value

    def __init__(self, user: str, passwd: str) -> None:
        self.manager: MerossManager
        self.client: MerossHttpClient
        asyncio.run(self.Start(user, passwd))

    @classmethod
    async def Start(cls, user: str, passwd: str) -> None:
        try:
            cls.client = await cls.StartClient(user, passwd)
            cls.manager = await cls.StartManager(cls.client)

        except Exception as exception:
            raise Exception({"Manager": exception.args[0]})

    @classmethod
    async def StartClient(cls, user: str, passwd: str) -> MerossHttpClient:
        return await MerossHttpClient.async_from_user_password(email=user, password=passwd)

    @classmethod
    async def StartManager(cls, client: MerossHttpClient) -> MerossManager:
        manager = MerossManager(http_client=client, auto_reconnect=True, mqtt_skip_cert_validation=True)
        await manager.async_init()
        return manager
