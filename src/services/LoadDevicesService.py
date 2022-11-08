import asyncio
from ..resource.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.DeviceType import DeviceType
from ..resource.repositories.DeviceRepositoryHelper import LoadDeviceHelper


def SearchDevices(user: str, passwd: str, deviceType: DeviceType) -> [Device]:
    result: [Device] = []

    try:
        devices = asyncio.run(DeviceRepository.LoadMerossDevices(user, passwd, deviceType))

        if (len(devices) > 0):
            for device in devices:
                outcome = LoadDeviceHelper.MapDevice(device)
                result.append(outcome)
                
    except Exception as e:
        print(f'Error when Load Meross Devices: {e}')

    return result
