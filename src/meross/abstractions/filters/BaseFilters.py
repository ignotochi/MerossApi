from meross.core.JsonHelper import JsonUtils
from dataclass_wizard import fromlist
from typing import TypeVar, List

T = TypeVar("T")


class BaseFilter:
    def __init__(self, data: str, dataClass: T) -> List[T]:

        self._parsedData: List[T] = []

        try:
            if len(data) > 0:
                parsedData: T = JsonUtils.ParseData(data)
                isArray = isinstance(parsedData, list)

                if isArray == True:
                    dataClassObj = fromlist(dataClass, parsedData)
            
                    for dataClass in dataClassObj:
                        self._parsedData.append(dataClass)

                else:
                    dataClassObj = fromlist(dataClass, [parsedData])
                    self._parsedData = dataClassObj[0]

        except Exception as exception:
            raise Exception({"BaseFilterError": "Error trying to parse data"})
