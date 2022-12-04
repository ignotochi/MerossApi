from meross.core.JsonHelper import JsonUtils
from dataclass_wizard import fromlist
from typing import TypeVar, List, Type

T = TypeVar("T")


class BaseFilter:
    def __init__(self, data: bytes, dataClass: T):

        self._parsedData: List[T] = []

        try:
            if data:
                parsedData: T = JsonUtils.ParseData(data, dataClass)
                isArray = isinstance(parsedData, list)

                if isArray is True:
                    dataClassObj = fromlist(dataClass, parsedData)
            
                    for dataClass in dataClassObj:
                        self._parsedData.append(dataClass)

                else:
                    dataClassObj = fromlist(dataClass, [parsedData])
                    self._parsedData = dataClassObj[0]

        except Exception as exception:
            raise Exception("Error trying to parse data")
