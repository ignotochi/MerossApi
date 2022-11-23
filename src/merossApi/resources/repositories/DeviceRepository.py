from merossApi.abstractions.IDevices import IDeviceRepository
from merossApi.abstractions import Device, ToggledDevice
from merossApi.abstractions.DeviceModel import DeviceModel
from merossApi.resources.manager.ManagerUtils import ManagerUtils
from merossApi.context.Context import Context
from typing import TypeVar, List

Device = TypeVar("Device")
ToggledDevice = TypeVar("ToggledDevice")


class DeviceRepository(IDeviceRepository):

    def LoadMerossDevices(context: Context, devices: DeviceModel) -> List[Device]:
        try:  
            result = []    
            
            result = ManagerUtils.GetDevices(context.manager, devices)
            
            return result

        except Exception as exception:
            raise Exception({"LoadMerossDevicesError" : exception.args[0]}) 

    def ToggleMerossDevice(context: Context, devices: List[ToggledDevice]) -> List[Device]:
        try:       
            result: List[str] = []

            for device in devices:
                updatedDeviceId = ManagerUtils.ToggleDevice(context.manager, device)
                
                if (updatedDeviceId != None):
                    result.append(updatedDeviceId)
                    
            return result

        except Exception as exception:
            raise {"ToggleMerossDeviceError" : exception.args[0]}
