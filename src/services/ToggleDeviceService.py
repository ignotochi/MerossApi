from ..resources.repositories.DeviceRepository import DeviceRepository
from ..abstractions.Device import Device
from ..abstractions.ToggledDevice import ToggledDevice
from ..context.context import Context


class ToggleDeviceService:

    @staticmethod
    def Toggle(devices: [ToggledDevice]) -> [str]:
        try:
            result: [str] = []
            context: Context = Context()
            
            result = DeviceRepository.ToggleMerossDevice(context, devices)
           
            return result

        except Exception as exception:
            return {"ToggleError": exception.args[0]}
