import asyncio
from ...abstractions.IDevices import IDeviceRepository
from ...abstractions import Device, ToggledDevice
from ...abstractions.DeviceModel import DeviceModel
from ...resources.manager.ManagerUtils import ManagerUtils
from ...context.context import Context

class DeviceRepository(IDeviceRepository):

    def LoadMerossDevices(devices: DeviceModel) -> [Device]:
        try:
            context = Context()
            
            result: [Device] = []

            result = asyncio.run(ManagerUtils.GetDevices(context.manager, devices))
            
            return result

        except Exception as exception:
            return {"LoadMerossDevicesError" : exception.args[0]}

    async def ToggleMerossDevice(devices: [ToggledDevice]) -> [Device]:
        try:
            context = Context()
            
            result: [str] = []

            for device in devices:
                updatedDeviceId = asyncio.run(ManagerUtils.ToggleDevice(context.manager, device))
                
                if (updatedDeviceId != None):
                    result.append(updatedDeviceId)

            return result

        except Exception as exception:
            return {"ToggleMerossDeviceError" : exception.args[0]}
