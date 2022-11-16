import asyncio
from ...abstractions.IDevices import IDeviceRepository
from ...abstractions import Device, ToggledDevice
from ...abstractions.DeviceType import DeviceType
from ...costatnts import *
from ..meross.ManagerUtils import ManagerUtils
from ...context.context import Context


class DeviceRepository(IDeviceRepository):

    def LoadMerossDevices(context: Context, devices: DeviceType) -> [Device]:
        try:
            result: [Device] = []

            result = asyncio.run(ManagerUtils.GetDevices(context, devices))
            
            return result

        except Exception as e:
            print(f'Error when Load Meross Devices: {e}')

    async def ToggleMerossDevice(context: Context, devices: [ToggledDevice]) -> [Device]:
        try:
            result: [str] = []

            for device in devices:
                updatedDeviceId = await ManagerUtils.ToggleDevice(Context, device)
                
                if (updatedDeviceId != None):
                    result.append(updatedDeviceId)

            return result

        except Exception as e:
            print(f'Error when Toglle Device Repository: {e}')
