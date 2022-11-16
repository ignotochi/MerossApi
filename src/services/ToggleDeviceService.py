import asyncio
from ..resource.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.ToggledDevice import ToggledDevice

class ToggleDeviceService: 
    
    @staticmethod
    def Toggle(devices: [ToggledDevice]) -> [str]:
        result: [str] = []

        try:
            result = asyncio.run(DeviceRepository.ToggleMerossDevice(devices))
            return result
        
        except Exception as e:
            print(f'Error when Toglle Device Service: {e}')
