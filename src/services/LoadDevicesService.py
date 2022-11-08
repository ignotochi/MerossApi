import asyncio
from ..resource.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.filters.DevicesFilter import DevicesFilter
from ..resource.repositories.DeviceRepositoryHelper import LoadDeviceHelper


def SearchDevices(user: str, passwd: str, filters: DevicesFilter) -> [Device]:
    result: [Device] = []

    try:
        devices = asyncio.run(DeviceRepository.LoadMerossDevices(user, passwd, filters))

        if (len(devices) > 0):
            for device in devices:
                outcome = LoadDeviceHelper.MapDevice(device)
                result.append(outcome)
                
    except Exception as e:
        print(f'Error when Load Meross Devices: {e}')

    return result
