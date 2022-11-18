from ..resources.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.ToggledDevice import ToggledDevice

class ToggleDeviceService: 
    
    @staticmethod
    def Toggle(devices: [ToggledDevice]) -> [str]:
        result: [str] = []

        try:
            result = DeviceRepository.ToggleMerossDevice(devices)
            return result
        
        except Exception as exception:
            return {"ToggleError" : exception.args[0]}
