import json
from typing import TypeVar

T = TypeVar("T")


class JsonUtils(object):

    @staticmethod
    def ParseData(data: str, dataClass: T) -> T:
        parsedData: dataClass = json.loads(data)
        return parsedData
