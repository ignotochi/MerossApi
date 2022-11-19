from dataclasses import dataclass


class Device:
    deviceName: str
    model: str
    firmwareVersion: str
    hardwareVersion: str
    deviceUid: str
    status: str


