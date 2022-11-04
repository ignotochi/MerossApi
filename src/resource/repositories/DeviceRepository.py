import asyncio
import os
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from ...abstractions.IDevices import IDeviceRepository
from ...costatnts import *
from ..meross.connection import ConnectionManager, Manager


class DeviceRepository(IDeviceRepository):

    async def LoadMerossDevices(user, passwd):
        result: Device = []
        
        try:        
            mng = await Manager(user, passwd).StartManager()

            if (mng):
                result = await mng.GetDevices(MSS_710)
            
            await mng.StopManagerAndLogOut()

        except Exception as e:
            print(f'Error when Load Meross Devices: {e}')
            await mng.StopManagerAndLogOut()

        return result

    async def ToggleMerossDevice(user, passwd):

        manager = manager(user, passwd)
