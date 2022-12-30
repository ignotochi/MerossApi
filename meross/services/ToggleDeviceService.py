from meross.abstractions.device import Device
from meross.resources.repositories.DeviceRepository import DeviceRepository
from meross.abstractions.device.ToggledDevice import ToggledDevice
from meross.abstractions.context.IContext import IContext
from typing import List

from meross.resources.repositories.DeviceRepositoryHelper import LoadDeviceHelper


class ToggleDeviceService:

    @staticmethod
    def Toggle(devices: List[ToggledDevice], context: IContext) -> List[Device]:
        try:
            result: List[Device] = []
            items = DeviceRepository.ToggleMerossDevice(context, devices)

            if items and len(items) > 0:
                for item in items:
                    outcome = LoadDeviceHelper.MapDevice(item)
                    result.append(outcome)

            return result

        except Exception as exception:
            raise Exception(str(exception.args[0]))
