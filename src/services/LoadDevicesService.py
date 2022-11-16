from ..resource.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.DeviceType import DeviceType
from ..resource.repositories.DeviceRepositoryHelper import LoadDeviceHelper

class LoadDevicesService:

    @staticmethod
    def Load(devices: DeviceType) -> [Device]:
        try:
            result: [Device] = []
            items = DeviceRepository.LoadMerossDevices(devices)

            if (len(items) > 0):
                for item in items:
                    outcome = LoadDeviceHelper.MapDevice(item)
                    result.append(outcome)
            
            return result
                    
        except Exception as e:
            print(f'Error when Load Meross Devices: {e}')
