from meross.abstractions.device.IDeviceRepository import IDeviceRepository
from meross.abstractions.device.Device import Device
from meross.abstractions.device.ToggledDevice import ToggledDevice
from meross.abstractions.device.DeviceModel import DeviceModel
from meross.resources.manager.ManagerUtils import ManagerUtils
from meross.abstractions.context.IContext import IContext
from typing import List
import asyncio


class DeviceRepository(IDeviceRepository):

    @staticmethod
    def LoadMerossDevices(context: IContext, devices: List[DeviceModel]) -> list[object]:
        try:
            result = ManagerUtils.GetDevices(context.manager, context.client, devices)
            return result

        except Exception as exception:
            raise Exception(exception.args[0])

    @staticmethod
    def ToggleMerossDevice(context: IContext, devices: List[ToggledDevice]) -> List[object]:
        try:
            result: List[object] = []

            for device in devices:
                item = ManagerUtils.ToggleDevice(context.manager, context.client, device)

                if item is not None:
                    result.append(item)

            return result

        except Exception as exception:
            raise Exception(exception.args[0])
