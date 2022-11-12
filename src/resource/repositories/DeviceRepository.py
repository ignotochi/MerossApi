import asyncio
import os
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from ...abstractions.IDevices import IDeviceRepository
from ...abstractions import Device, ToggledDevice
from ...abstractions.DeviceType import DeviceType
from ...costatnts import *
from ..meross.ManagerUtils import ManagerUtils, Manager


class DeviceRepository(IDeviceRepository):

    async def LoadMerossDevices(deviceType: DeviceType) -> [Device]:
        try:
            result: [Device] = []

            mng = await Manager().StartManager()

            if (mng):
                result = await mng.GetDevices(deviceType)

            #await mng.StopManagerAndLogOut()

            return result

        except Exception as e:
            print(f'Error when Load Meross Devices: {e}')

    async def ToggleMerossDevice(toggledDevices: [ToggledDevice]) -> [Device]:
        try:
            result: [str] = []

            mng = await Manager().StartManager()

            if (mng):
                for toggledDevice in toggledDevices:
                    updatedDeviceId = await mng.ToggleDevice(toggledDevice)
                    result.append(updatedDeviceId)

            await mng.StopManagerAndLogOut()

            return result

        except Exception as e:
            print(f'Error when Toglle Device Repository: {e}')
