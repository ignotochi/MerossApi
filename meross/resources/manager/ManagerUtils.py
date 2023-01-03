from asyncio import AbstractEventLoop
from meross.abstractions.device.DeviceModel import DeviceModel
from meross.abstractions.device.ToggledDevice import ToggledDevice
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross.core.exeptions.customException import CustomException
from meross.core.logger import MerossLogger
from meross.core.wraps import UpdateLoopManager
from typing import List


class ManagerUtils:

    @staticmethod
    @UpdateLoopManager
    async def GetDevices(manager: MerossManager, client: MerossHttpClient, devices: List[DeviceModel]) -> List[object]:
        try:
            result: List[object] = []
            await manager.async_device_discovery()

            for device in devices:
                dev: DeviceModel = device

                if len(devices) > 0:
                    discoveredDevices = manager.find_devices(device_type=dev.model)
                else:
                    discoveredDevices = manager.find_devices()

                if discoveredDevices and len(discoveredDevices) > 0:
                    for discoveredDevice in discoveredDevices:
                        await discoveredDevice.async_update()
                        result.append(discoveredDevice)

            return result

        except Exception as exception:
            MerossLogger("ManagerUtils.GetDevices").WriteErrorLog(exception.args[0])
            CustomException.TimeOutExceptionOrRaise(exception, f"Error trying to get devices: {str(devices)}")
            await ManagerUtils.StopManagerAndLogOut(manager, client)

    @staticmethod
    @UpdateLoopManager
    async def TestConnection(manager: MerossManager, client: MerossHttpClient) -> bool:
        try:
            discoverDevices = await manager.async_device_discovery()
            foundedDevices = manager.find_devices()

            if discoverDevices is not None and foundedDevices is not None:
                for discoverDevice in discoverDevices:
                    await discoverDevice.async_update()

                return True

        except Exception as exception:
            MerossLogger("ManagerUtils.TestConnection").WriteErrorLog(exception.args[0])
            await ManagerUtils.StopManagerAndLogOut(manager, client)
            return False

    @staticmethod
    @UpdateLoopManager
    async def ToggleDevice(manager: MerossManager, client: MerossHttpClient, toggledDevice: ToggledDevice) -> object:
        try:
            await manager.async_device_discovery()
            device = manager.find_devices(toggledDevice.deviceId)[0]

            if toggledDevice.enabled:
                await device.async_turn_on(channel=0)
            else:
                await device.async_turn_off(channel=0)

            await device.async_update()

            return device

        except Exception as exception:
            MerossLogger("ManagerUtils.ToggleDevice").WriteErrorLog(exception.args[0])
            CustomException.TimeOutExceptionOrRaise(exception, f"Error trying to toggle device: {toggledDevice.deviceId}")
            await ManagerUtils.StopManagerAndLogOut(manager, client)

    @staticmethod
    async def StopManagerAndLogOut(manager: MerossManager, client: MerossHttpClient) -> bool:
        try:
            manager.close()
            await client.async_logout()
            return manager.http_client.cloud_credentials is None

        except Exception as exception:
            MerossLogger("ManagerUtils.ToggleDevice").WriteErrorLog(exception.args[0])
            raise Exception("Error trying to stop manager and logout")
