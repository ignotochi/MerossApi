from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger
from meross.resources.repositories.DeviceRepository import DeviceRepository
from meross.abstractions.device.Device import Device
from meross.abstractions.device.DeviceModel import DeviceModel
from meross.abstractions.context.IContext import IContext
from meross.resources.repositories.DeviceRepositoryHelper import LoadDeviceHelper
from typing import List


class LoadDevicesService:

    @staticmethod
    async def Load(devices: List[DeviceModel], context: IContext) -> List[Device]:
        try:
            result: List[Device] = []
            items = await DeviceRepository.LoadMerossDevices(context, devices)

            if items and len(items) > 0:
                for item in items:
                    outcome = LoadDeviceHelper.MapDevice(item)
                    result.append(outcome)

            return result

        except Exception as exception:
            MerossLogger("LoadDevicesService.Load").WriteErrorLog(ExceptionManager.TryToCatch(exception))
            raise Exception(ExceptionManager.TryToCatch(exception))
