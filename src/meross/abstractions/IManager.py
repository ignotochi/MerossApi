from abc import ABC, abstractmethod
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient

class IManager(ABC, object):

    @property
    @abstractmethod
    def client(self) -> MerossHttpClient: 
        pass

    @property
    @abstractmethod
    def manager(self) -> MerossManager: 
        pass

    @abstractmethod
    def Start() -> None:
        pass
    
    @abstractmethod
    def __StartClient(value) -> MerossHttpClient:
        pass

    @abstractmethod
    def __StartManager() -> MerossManager:
        pass

    @abstractmethod
    def Reset() -> None:
        pass

