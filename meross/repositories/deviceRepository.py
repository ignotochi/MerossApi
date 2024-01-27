from meross.abstractions.device.deviceRepository_interface import IDeviceRepository
from meross.abstractions.device.toggledDevice import ToggledDevice
from meross.abstractions.device.deviceModel import deviceModel
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger
from meross.abstractions.context.context_interface import IContext
from meross.manager.manager import Manager
from typing import List


class DeviceRepository(IDeviceRepository):

    @staticmethod
    async def loadMerossDevices(context: IContext, devices: List[deviceModel]) -> list[object]:
        try:
            result = await Manager.getDevices(context.manager, context.client, devices)
            return result

        except Exception as exception:
            MerossLogger("DeviceRepository.loadMerossDevices").writeErrorLog(ExceptionManager.catch(exception))
            raise Exception(ExceptionManager.catch(exception))

    @staticmethod
    async def toggleMerossDevice(context: IContext, devices: List[ToggledDevice]) -> List[object]:
        try:
            result: List[object] = []

            for device in devices:
                item = await Manager.toggleDevice(context.manager, context.client, device)

                if item is not None:
                    result.append(item)

            return result

        except Exception as exception:
            MerossLogger("DeviceRepository.toggleMerossDevice").writeErrorLog(ExceptionManager.catch(exception))
            raise Exception(exception.args[0])
