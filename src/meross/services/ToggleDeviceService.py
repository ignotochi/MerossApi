from meross.resources.repositories.DeviceRepository import DeviceRepository
from meross.abstractions.ToggledDevice import ToggledDevice
from meross.context.Context import Context
from typing import TypeVar, List

ToggledDevice = TypeVar("ToggledDevice")

class ToggleDeviceService:

    @staticmethod
    def Toggle(devices: List[ToggledDevice]) -> List[str]:
        try:
            result: List[str] = []
            context: Context = Context()
            
            result = DeviceRepository.ToggleMerossDevice(context, devices)
           
            return result

        except Exception as exception:
            return {"ToggleError": exception.args[0]}
