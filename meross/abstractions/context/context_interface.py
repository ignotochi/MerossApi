from abc import ABC, abstractmethod
from datetime import datetime
from cryptography.fernet import Fernet
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient


class IContext(ABC, object):

    @abstractmethod
    def getToken(self) -> str:
        pass

    @abstractmethod
    def encrypt(self, value: str) -> str:
        pass

    @abstractmethod
    def decryptLocalToken(self) -> str:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def setSessionActivityLastTimeCheck(self, value) -> None:
        pass
