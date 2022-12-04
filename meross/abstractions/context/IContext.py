from abc import ABC, abstractmethod
from cryptography.fernet import Fernet
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient


class IContext(ABC, object):

    @property
    @abstractmethod
    def fernet(self, value) -> Fernet:
        pass

    @property
    @abstractmethod
    def token(self, value) -> str:
        pass

    @property
    @abstractmethod
    def authenticated(self, value) -> bool:
        pass

    @property
    @abstractmethod
    def client(self, value) -> MerossHttpClient:
        pass

    @property
    @abstractmethod
    def manager(self, value) -> MerossManager:
        pass

    @abstractmethod
    def GetToken(self) -> str:
        pass

    @abstractmethod
    def Encrypt(self, value: str) -> str:
        pass

    @abstractmethod
    def DecryptLocalToken(self) -> str:
        pass

    @abstractmethod
    def Reset(self) -> None:
        pass
