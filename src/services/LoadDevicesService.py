from ..resources.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.DeviceModel import DeviceModel
from ..resources.repositories.DeviceRepositoryHelper import LoadDeviceHelper
from ..context.context import Context

class LoadDevicesService:

    @staticmethod
    def Load(devices: DeviceModel) -> [Device]:
        try:
            result: [Device] = []
            
            context: Context = Context()
            
            items = DeviceRepository.LoadMerossDevices(context, devices)

            if (items and len(items) > 0):
                for item in items:
                    outcome = LoadDeviceHelper.MapDevice(item)
                    result.append(outcome)
            
            return result
                    
        except Exception as exception:
            return {"LoadError" : exception.args[0]}
