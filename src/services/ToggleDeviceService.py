import asyncio
from ..resource.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.ToggledDevice import ToggledDevice

def ToggleDevice(user: str, passwd: str, toggledDevices: [ToggledDevice]):
    result: [str] = []

    try:
        result = asyncio.run(DeviceRepository.ToggleMerossDevice(user, passwd, toggledDevices))
    except Exception as e:
        print(f'Error when Toglle Device Service: {e}')

    return result