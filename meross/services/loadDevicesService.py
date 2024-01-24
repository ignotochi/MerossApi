from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger
from meross.repositories.deviceRepository import DeviceRepository
from meross.repositories.deviceRepositoryHelper import LoadDeviceHelper
from meross.abstractions.device.device import device
from meross.abstractions.device.deviceModel import deviceModel
from meross.abstractions.context.context_interface import IContext
from typing import List


class LoadDevicesService:

    @staticmethod
    async def load(devices: List[deviceModel], context: IContext) -> List[device]:
        try:
            result: List[device] = []
            items = await DeviceRepository.loadMerossDevices(context, devices)

            if items and len(items) > 0:
                for item in items:
                    outcome = LoadDeviceHelper.MapDevice(item)
                    result.append(outcome)

            return result

        except Exception as exception:
            MerossLogger("LoadDevicesService.load").writeErrorLog(ExceptionManager.catch(exception))
            raise Exception(ExceptionManager.catch(exception))
