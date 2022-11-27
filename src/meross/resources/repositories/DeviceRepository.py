from meross.abstractions.IDevices import IDeviceRepository
from meross.abstractions.Device import Device
from meross.abstractions.ToggledDevice import ToggledDevice
from meross.abstractions.DeviceModel import DeviceModel
from meross.resources.manager.ManagerUtils import ManagerUtils
from meross.abstractions.iContext import IContext
from typing import List


class DeviceRepository(IDeviceRepository):

    @staticmethod
    def LoadMerossDevices(context: IContext, devices: List[DeviceModel]) -> List[Device]:
        try:  
            result: List[Device] = []  

            result = ManagerUtils.GetDevices(context.manager, devices)
            
            return result

        except Exception as exception:
            raise Exception({"LoadMerossDevicesError" : exception.args[0]}) 

    
    @staticmethod
    def ToggleMerossDevice(context: IContext, devices: List[ToggledDevice]) -> List[str]:
        try:       
            result: List[str] = []

            for device in devices:
                updatedDeviceId = ManagerUtils.ToggleDevice(context.manager, device)
                
                if (updatedDeviceId != None):
                    result.append(str(updatedDeviceId))
                    
            return result

        except Exception as exception:
            raise Exception({"ToggleMerossDeviceError" : exception.args[0]})
