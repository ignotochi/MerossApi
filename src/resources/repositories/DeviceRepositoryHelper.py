from ...abstractions.Device import Device

class LoadDeviceHelper:

    @staticmethod
    def MapDevice(item):
        outcome: Device = Device()

        outcome.deviceName = item.name
        outcome.deviceType = item.type
        outcome.hardwareVersion = item.hardware_version
        outcome.firmwareVersion = item.firmware_version
        outcome.deviceId = item.uuid
        outcome.status = item.online_status.name

        return outcome
