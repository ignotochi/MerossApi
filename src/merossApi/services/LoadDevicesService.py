from merossApi.resources.repositories.DeviceRepository import DeviceRepository
from merossApi.abstractions.Device import Device
from merossApi.abstractions.DeviceModel import DeviceModel
from merossApi.resources.repositories.DeviceRepositoryHelper import LoadDeviceHelper
from merossApi.context.Context import Context
from typing import TypeVar, List

Device = TypeVar("Device")

class LoadDevicesService:

    @staticmethod
    def Load(devices: DeviceModel) -> List[Device]:
        try:
            result: List[Device] = []
            
            context: Context = Context()
            
            items = DeviceRepository.LoadMerossDevices(context, devices)

            if (items and len(items) > 0):
                for item in items:
                    outcome = LoadDeviceHelper.MapDevice(item)
                    result.append(outcome)
            
            return result
                    
        except Exception as exception:
            return {"LoadError" : exception.args[0]}
