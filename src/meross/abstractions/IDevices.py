from abc import ABC, abstractmethod

class IDeviceRepository(ABC):

    @abstractmethod
    def LoadMerossDevices(user, passwd):
        pass
    
    @abstractmethod
    def ToggleMerossDevice(user, passwd):
        pass
    
    
