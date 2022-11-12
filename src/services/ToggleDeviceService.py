import asyncio
from ..resource.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.ToggledDevice import ToggledDevice

def ToggleDeviceService(toggledDevices: [ToggledDevice]) -> [str]:
    result: [str] = []

    try:
        result = asyncio.run(DeviceRepository.ToggleMerossDevice(toggledDevices))
        return result
    
    except Exception as e:
        print(f'Error when Toglle Device Service: {e}')
