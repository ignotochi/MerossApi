import asyncio
from ...abstractions.IDevices import IDeviceRepository
from ...abstractions import Device, ToggledDevice
from ...abstractions.DeviceModel import DeviceModel
from ...resources.manager.ManagerUtils import ManagerUtils
from ...context.context import Context

class DeviceRepository(IDeviceRepository):

    def LoadMerossDevices(context: Context, devices: DeviceModel) -> [Device]:
        try:  
            result: [Device] = []    
            
            result = ManagerUtils.GetDevices(context.manager, devices)
            
            return result

        except Exception as exception:
            raise Exception({"LoadMerossDevicesError" : exception.args[0]}) 

    def ToggleMerossDevice(context: Context, devices: [ToggledDevice]) -> [Device]:
        try:       
            result: [str] = []

            for device in devices:
                updatedDeviceId = ManagerUtils.ToggleDevice(context.manager, device)
                
                if (updatedDeviceId != None):
                    result.append(updatedDeviceId)
                    
            return result

        except Exception as exception:
            raise {"ToggleMerossDeviceError" : exception.args[0]}
