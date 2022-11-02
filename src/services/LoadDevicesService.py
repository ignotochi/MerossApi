import asyncio
from ..repository.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..repository.DeviceRepositoryHelper import LoadDeviceHelper


def SearchDevices(user, passwd):
    result: Device = []
    devices: object()

    try:
        devices = asyncio.run(DeviceRepository.LoadMerossDevices(user, passwd))
    except:
        print("Error when Load Meross Devices")

    if (len(devices) > 0):
        for device in devices:
            outcome = LoadDeviceHelper.MapDevice(device)
            result.append(outcome)

    return result
