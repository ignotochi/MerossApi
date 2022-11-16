import asyncio
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from ...abstractions.IDevices import IDeviceRepository
from ...abstractions import Device, ToggledDevice
from ...abstractions.DeviceType import DeviceType
from ...costatnts import *
from ...context.context import Context
from ..meross.ManagerUtils import ManagerUtils


class DeviceRepository(IDeviceRepository):

    def LoadMerossDevices(devices: DeviceType) -> [Device]:
        try:
            result: [Device] = []

            result = asyncio.run(ManagerUtils.GetDevices(Context.manager, devices))

            return result

        except Exception as e:
            print(f'Error when Load Meross Devices: {e}')

    async def ToggleMerossDevice(devices: [ToggledDevice]) -> [Device]:
        try:
            result: [str] = []

            for device in devices:
                updatedDeviceId = await ManagerUtils.ToggleDevice(Context.manager, device)
                if (updatedDeviceId != None):
                    result.append(updatedDeviceId)

            return result

        except Exception as e:
            print(f'Error when Toglle Device Repository: {e}')
