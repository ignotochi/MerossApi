from abc import ABC, abstractmethod
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient

class IContext(ABC, object):

    @property
    @abstractmethod
    def authenticated(self) -> bool: 
        pass

    @property
    @abstractmethod
    def client(self) -> MerossHttpClient: 
        pass

    @property
    @abstractmethod
    def manager(self) -> MerossManager: 
        pass

    @abstractmethod
    def GetToken() -> str:
        pass
    
    @abstractmethod
    def __Encrypt(value) -> str:
        pass

    @abstractmethod
    def DecryptLocalToken() -> str:
        pass

    @abstractmethod
    def Reset() -> None:
        pass
