import asyncio
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross.abstractions.manager.manager_interface import IManager
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger


class MerossIotManager(IManager):

    def manager(self, value):
        self.manager = value

    def client(self, value):
        self.client = value

    def __init__(self, user: str, passwd: str) -> None:
        self.manager: MerossManager
        self.client: MerossHttpClient
        asyncio.run(self.start(user, passwd))

    @classmethod
    async def start(cls, user: str, passwd: str) -> None:
        try:
            cls.client = await cls.startClient(user, passwd)
            cls.manager = await cls.startManager(cls.client)

        except Exception as exception:
            MerossLogger("Singleton.start").writeErrorLog(ExceptionManager.catch(exception))
            raise Exception("Manager did not start")

    @classmethod
    async def startClient(cls, user: str, passwd: str) -> MerossHttpClient:
        return await MerossHttpClient.async_from_user_password(api_base_url='https://iotx-eu.meross.com', email=user, password=passwd)

    @classmethod
    async def startManager(cls, client: MerossHttpClient) -> MerossManager:
        manager = MerossManager(http_client=client, auto_reconnect=True, mqtt_skip_cert_validation=True)
        await manager.async_init()
        return manager
