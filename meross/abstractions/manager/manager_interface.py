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
    def start(self, user: str, passwd: str) -> None:
        pass

    @abstractmethod
    def startClient(self, user: str, passwd: str) -> MerossHttpClient:
        pass

    @abstractmethod
    def startManager(self, client: MerossHttpClient) -> MerossManager:
        pass
