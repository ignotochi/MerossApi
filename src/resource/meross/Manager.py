from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient

class Manager():
    
    manager: MerossManager = None
    client: MerossHttpClient = None
        
    @classmethod
    async def Start(self, user: str, passwd: str) -> None:
       
        newIstanceNeeded = isinstance(self.manager, MerossManager) == False and isinstance(self.client, MerossHttpClient) == False
        
        if (newIstanceNeeded):
            await self.__StartClient(user, passwd)
            await self.__StartManager()
                             
    @classmethod
    async def __StartClient(self, user: str, passwd: str) -> None:
        self.client = await MerossHttpClient.async_from_user_password(email=user, password=passwd)
    
    @classmethod
    async def __StartManager(self) -> None:
        self.manager = MerossManager(http_client = self.client)
        await self.manager.async_init()
        
    @classmethod
    def GetClient(self) -> MerossHttpClient:
        return self.client

