import asyncio
from ...abstractions.IDevices import IDeviceRepository
from ...abstractions import Device, ToggledDevice
from ...abstractions.DeviceType import DeviceType
from ...costatnts import *
from ..meross.ManagerUtils import ManagerUtils
from ..meross.Manager import Manager


class DeviceRepository(IDeviceRepository):

    def LoadMerossDevices(manager: Manager, devices: DeviceType) -> [Device]:
        try:
            result: [Device] = []

            result = asyncio.run(ManagerUtils.GetDevices(manager, devices))
            
            return result

        except Exception as e:
            print(f'Error when Load Meross Devices: {e}')

    async def ToggleMerossDevice(manager: Manager, devices: [ToggledDevice]) -> [Device]:
        try:
            result: [str] = []

            for device in devices:
                updatedDeviceId = await ManagerUtils.ToggleDevice(Conmanagertext, device)
                
                if (updatedDeviceId != None):
                    result.append(updatedDeviceId)

            return result

        except Exception as e:
            print(f'Error when Toglle Device Repository: {e}')
