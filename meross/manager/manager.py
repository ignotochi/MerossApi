from asyncio import AbstractEventLoop
from meross.abstractions.device.deviceModel import deviceModel
from meross.abstractions.device.toggledDevice import ToggledDevice
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger
from meross.core.wraps import UpdateLoopManager
from typing import List


class Manager:

    @staticmethod
    @UpdateLoopManager
    async def getDevices(manager: MerossManager, client: MerossHttpClient, devices: List[deviceModel]) -> List[object]:
        try:
            result: List[object] = []
            await manager.async_device_discovery()

            for device in devices:
                dev: deviceModel = device

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
            MerossLogger("ManagerUtils.getDevices").writeErrorLog(ExceptionManager.catch(exception))
            ExceptionManager.timeOutExceptionOrRaise(exception, f"Error trying to get devices: {str(devices)}")
            await Manager.stopManagerAndLogOut(manager, client)

    @staticmethod
    @UpdateLoopManager
    async def testManagerConnection(manager: MerossManager, client: MerossHttpClient) -> bool:
        try:
            discoverDevices = await manager.async_device_discovery()
            foundedDevices = manager.find_devices()

            if discoverDevices is not None and foundedDevices is not None:
                for discoverDevice in discoverDevices:
                    await discoverDevice.async_update()

                return True

        except Exception as exception:
            MerossLogger("ManagerUtils.testManagerConnection").writeErrorLog(ExceptionManager.catch(exception))
            await Manager.stopManagerAndLogOut(manager, client)
            return False

    @staticmethod
    @UpdateLoopManager
    async def toggleDevice(manager: MerossManager, client: MerossHttpClient, toggledDevice: ToggledDevice) -> object:
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
            MerossLogger("ManagerUtils.toggleDevice").writeErrorLog(ExceptionManager.catch(exception))
            ExceptionManager.timeOutExceptionOrRaise(exception, f"Error trying to toggle device: {toggledDevice.deviceId}")
            await Manager.stopManagerAndLogOut(manager, client)

    @staticmethod
    async def stopManagerAndLogOut(manager: MerossManager, client: MerossHttpClient) -> bool:
        try:
            await client.async_logout()
            return client.cloud_credentials is None

        except Exception as exception:
            MerossLogger("ManagerUtils.stopManagerAndLogOut").writeErrorLog(exception.args[0])
            raise Exception("Error trying to stop manager and logout")
