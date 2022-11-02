import asyncio
from ..meross.LoadDevices.LoadDevices import Devices
from ..abstractions.Device import Device
from ..meross.LoadDevices.LoadDeviceHelepr import LoadDeviceHelper


def searchDevices(user, passwd):
    devices: object()

    try:
        devices = asyncio.run(Devices.LoadMerossDevices(user, passwd))
    except:
        print("Error when Load Meross Devices")

    result: Device = []

    for device in devices:
        outcome = LoadDeviceHelper.MapDevice(device)
        result.append(outcome)

    return result
