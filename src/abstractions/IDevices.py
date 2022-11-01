from abc import ABC, abstractmethod

class IDevices(ABC):

    @abstractmethod
    def LoadMerossDevices(user, passwd):
        pass
    
    
