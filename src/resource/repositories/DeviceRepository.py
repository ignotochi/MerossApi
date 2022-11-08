import asyncio
import os
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from ...abstractions.IDevices import IDeviceRepository
from ...abstractions import Device, ToggledDevice
from ...abstractions.filters.DevicesFilter import DevicesFilter
from ...costatnts import *
from ..meross.ManagerUtils import ManagerUtils, Manager


class DeviceRepository(IDeviceRepository):

    async def LoadMerossDevices(user: str, passwd: str, filters: DevicesFilter) -> [Device]:
        result: [Device] = []
        
        try:        
            mng = await Manager(user, passwd).StartManager()    
                
            if (mng):
                result = await mng.GetDevices(filters.devices)         
                 
            await mng.StopManagerAndLogOut()
                 
        except Exception as e:
            print(f'Error when Load Meross Devices: {e}')    
       
        return result

    async def ToggleMerossDevice(user: str, passwd: str, toggledDevices: [ToggledDevice]) -> [Device]:
        result: [str] = []
        
        try:        
            mng = await Manager(user, passwd).StartManager()
            
            if (mng):    
                for toggledDevice in toggledDevices:
                 updatedDeviceId = await mng.ToggleDevice(toggledDevice)
                 result.append(updatedDeviceId)
            
            await mng.StopManagerAndLogOut()

        except Exception as e:
            print(f'Error when Toglle Device Repository: {e}')

        return result
