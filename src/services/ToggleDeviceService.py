import asyncio
from ..resources.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.ToggledDevice import ToggledDevice
from ..context.context import Context

class ToggleDeviceService: 
    
    @staticmethod
    def Toggle(devices: [ToggledDevice]) -> [str]:
        result: [str] = []
        
        context = Context

        try:
            result = asyncio.run(DeviceRepository.ToggleMerossDevice(context, devices))
            return result
        
        except Exception as e:
            print(f'Error when Toglle Device Service: {e}')
