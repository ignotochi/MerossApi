import asyncio
from ..resource.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..resource.repositories.DeviceRepositoryHelper import LoadDeviceHelper


def SearchDevices(user, passwd):
    result: Device = []

    try:
        items = asyncio.run(DeviceRepository.LoadMerossDevices(user, passwd))

        if (len(items) > 0):
            for item in items:
                outcome = LoadDeviceHelper.MapDevice(item)
                result.append(outcome)
                
    except Exception as e:
        print(f'Error when Load Meross Devices: {e}')

    return result
