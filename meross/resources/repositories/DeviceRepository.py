from meross.abstractions.device.IDeviceRepository import IDeviceRepository
from meross.abstractions.device.Device import Device
from meross.abstractions.device.ToggledDevice import ToggledDevice
from meross.abstractions.device.DeviceModel import DeviceModel
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger
from meross.resources.manager.ManagerUtils import ManagerUtils
from meross.abstractions.context.IContext import IContext
from typing import List
import asyncio


class DeviceRepository(IDeviceRepository):

    @staticmethod
    async def LoadMerossDevices(context: IContext, devices: List[DeviceModel]) -> list[object]:
        try:
            result = await ManagerUtils.GetDevices(context.manager, context.client, devices)
            return result

        except Exception as exception:
            MerossLogger("DeviceRepository.LoadMerossDevices").WriteErrorLog(ExceptionManager.TryToCatch(exception))
            raise Exception(ExceptionManager.TryToCatch(exception))

    @staticmethod
    async def ToggleMerossDevice(context: IContext, devices: List[ToggledDevice]) -> List[object]:
        try:
            result: List[object] = []

            for device in devices:
                item = await ManagerUtils.ToggleDevice(context.manager, context.client, device)

                if item is not None:
                    result.append(item)

            return result

        except Exception as exception:
            MerossLogger("DeviceRepository.ToggleMerossDevice").WriteErrorLog(ExceptionManager.TryToCatch(exception))
            raise Exception(exception.args[0])
