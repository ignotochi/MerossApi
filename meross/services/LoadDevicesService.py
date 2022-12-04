from meross.resources.repositories.DeviceRepository import DeviceRepository
from meross.abstractions.device.Device import Device
from meross.abstractions.device.DeviceModel import DeviceModel
from meross.abstractions.context.IContext import IContext
from meross.resources.repositories.DeviceRepositoryHelper import LoadDeviceHelper
from typing import List, Union


class LoadDevicesService:

    @staticmethod
    def Load(devices: List[DeviceModel], context: IContext) -> Union[List[Device], str]:
        try:
            result: List[Device] = []
            items = DeviceRepository.LoadMerossDevices(context, devices)

            if items and len(items) > 0:
                for item in items:
                    outcome = LoadDeviceHelper.MapDevice(item)
                    result.append(outcome)

            return result

        except Exception as exception:
            return "LoadError: " + str(exception.args[0])
