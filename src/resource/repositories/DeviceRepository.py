from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from ...abstractions.IDevices import IDeviceRepository
from ...abstractions import Device, ToggledDevice
from ...abstractions.DeviceType import DeviceType
from ...costatnts import *
from ...context.context import Context
from ..meross.ManagerUtils import ManagerUtils


class DeviceRepository(IDeviceRepository):

    async def LoadMerossDevices(deviceType: DeviceType) -> [Device]:
        try:
            result: [Device] = []
            
            result = await ManagerUtils.GetDevices(Context.manager, deviceType)
            
            # await mng.StopManagerAndLogOut()
            
            return result

        except Exception as e:
            print(f'Error when Load Meross Devices: {e}')

    async def ToggleMerossDevice(toggledDevices: [ToggledDevice]) -> [Device]:
        try:
            result: [str] = []

            for toggledDevice in toggledDevices:
                updatedDeviceId = await ManagerUtils.ToggleDevice(Context.manager, toggledDevice)
                result.append(updatedDeviceId)

            # await mng.StopManagerAndLogOut()

            return result

        except Exception as e:
            print(f'Error when Toglle Device Repository: {e}')
