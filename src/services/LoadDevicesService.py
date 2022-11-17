from ..resources.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.DeviceType import DeviceType
from ..resources.repositories.DeviceRepositoryHelper import LoadDeviceHelper
from ..context.context import Context

class LoadDevicesService:

    @staticmethod
    def Load(devices: DeviceType) -> [Device]:
        try:
            result: [Device] = []
            
            items = DeviceRepository.LoadMerossDevices(Context.managerTools.manager, devices)

            if (len(items) > 0):
                for item in items:
                    outcome = LoadDeviceHelper.MapDevice(item)
                    result.append(outcome)
            
            return result
                    
        except Exception as e:
            print(f'Error when Load Meross Devices: {e}')
