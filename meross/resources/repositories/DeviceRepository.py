from meross.abstractions.device.IDeviceRepository import IDeviceRepository
from meross.abstractions.device.Device import Device
from meross.abstractions.device.ToggledDevice import ToggledDevice
from meross.abstractions.device.DeviceModel import DeviceModel
from meross.resources.manager.ManagerUtils import ManagerUtils
from meross.abstractions.context.IContext import IContext
from typing import List


class DeviceRepository(IDeviceRepository):

    @staticmethod
    def LoadMerossDevices(context: IContext, devices: List[DeviceModel]) -> list[Device]:
        try:
            result = ManagerUtils.GetDevices(context.manager, context.client, devices)
            return result

        except Exception as exception:
            raise Exception("LoadMerossDevicesError: " + exception.args[0])

    @staticmethod
    def ToggleMerossDevice(context: IContext, devices: List[ToggledDevice]) -> List[str]:
        try:
            result: List[str] = []

            for device in devices:
                updatedDeviceId = ManagerUtils.ToggleDevice(context.manager, context.client, device)

                if updatedDeviceId is not None:
                    result.append(str(updatedDeviceId))

            return result

        except Exception as exception:
            raise Exception("ToggleMerossDeviceError: " + exception.args[0])
