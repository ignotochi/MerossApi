import asyncio
from ..resource.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.DeviceType import DeviceType
from ..resource.repositories.DeviceRepositoryHelper import LoadDeviceHelper


def LoadDevicesService(deviceType: DeviceType) -> [Device]:
    try:
        result: [Device] = []
        devices = asyncio.run(DeviceRepository.LoadMerossDevices(deviceType))

        if (len(devices) > 0):
            for device in devices:
                outcome = LoadDeviceHelper.MapDevice(device)
                result.append(outcome)
        
        return result
                
    except Exception as e:
        print(f'Error when Load Meross Devices: {e}')
