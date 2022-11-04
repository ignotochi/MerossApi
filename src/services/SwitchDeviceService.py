import asyncio
from ..resource.repositories.DeviceRepository import DeviceRepository

def ToggleDevice(user, passwd):
    devices: None

    try:
        devices = asyncio.run(DeviceRepository.ToggleMerossDevice(user, passwd))
    except:
        print("Error when Load Meross Devices")

    result: Device = []


    return result