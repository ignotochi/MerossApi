from ..resources.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.DeviceModel import DeviceModel
from ..resources.repositories.DeviceRepositoryHelper import LoadDeviceHelper

class LoadDevicesService:

    @staticmethod
    def Load(devices: DeviceModel) -> [Device]:
        try:
            result: [Device] = []
            
            items = DeviceRepository.LoadMerossDevices(devices)

            if (len(items) > 0):
                for item in items:
                    outcome = LoadDeviceHelper.MapDevice(item)
                    result.append(outcome)
            
            return result
                    
        except Exception as exception:
            return {"LoadError" : exception.args[0]}
