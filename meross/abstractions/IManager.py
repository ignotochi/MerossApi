from abc import ABC, abstractmethod
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient

class IManager(ABC, object):

    @property
    @abstractmethod
    def client(self, value) -> MerossHttpClient:
        pass

    @property
    @abstractmethod
    def manager(self, value) -> MerossManager:
        pass

    @abstractmethod
    @classmethod
    def Start(cls, user: str, passwd: str) -> None:
        pass
    
    @abstractmethod
    @classmethod
    def __StartClient(cls, user: str, passwd: str) -> MerossHttpClient:
        pass

    @abstractmethod
    @classmethod
    def __StartManager(cls, client: MerossHttpClient) -> MerossManager:
        pass

    @abstractmethod
    @classmethod
    def Reset(cls) -> None:
        pass

