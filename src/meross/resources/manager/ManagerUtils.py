from meross.abstractions.DeviceModel import DeviceModel
from meross.abstractions.Device import Device
from meross.abstractions.ToggledDevice import ToggledDevice
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross.core.wraps import UpdateLoopManager
from typing import TypeVar, List

DeviceModel = TypeVar("DeviceModel")
Device = TypeVar("Device")

class ManagerUtils():

    @UpdateLoopManager
    async def GetDevices(manager: MerossManager, devices: List[DeviceModel]) -> List[Device]:
        try:
            result: List[Device] = []

            await manager.async_device_discovery()

            for device in devices:
                dev: DeviceModel = device

                discoveredDevices = manager.find_devices(
                    device_type=dev.model)

                if (discoveredDevices and len(discoveredDevices) > 0):

                    for discoveredDevice in discoveredDevices:
                        await discoveredDevice.async_update()
                        result.append(discoveredDevice)

            return result

        except Exception as exception:
            raise Exception(exception.args[0])


    @UpdateLoopManager
    async def ToggleDevice(manager: MerossManager, toggledDevice: ToggledDevice) -> str:
        try:
            deviceId: str = None

            await manager.async_device_discovery()
            device = manager.find_devices(toggledDevice.deviceId)[0]
            deviceId = device.uuid

            if (toggledDevice.enabled == True):
                await device.async_turn_on(channel=0)
            else:
                await device.async_turn_off(channel=0)

            await device.async_update()
            return deviceId

        except Exception as exception:
            raise Exception(exception.args[0])


    @staticmethod
    async def StopManagerAndLogOut(manager: MerossManager, client: MerossHttpClient) -> bool:
        try:
            manager.close()
            await client.async_logout()
            return (manager._http_client._cloud_creds == None)

        except Exception as exception:
            raise Exception(exception.args[0])
