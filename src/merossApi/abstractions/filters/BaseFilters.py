from merossApi.core.JsonHelper import JsonUtils
from dataclass_wizard import fromlist
from typing import TypeVar

T = TypeVar("T")


class BaseFilter:
    def __init__(self, data: str, dataClass: T) -> T:

        try:
            if len(data) > 0:
                parsedData: T = JsonUtils.ParseData(data)
                isArray = isinstance(parsedData, list)

                if isArray == True:
                    dataClassObj = fromlist(dataClass, parsedData)
                    items = []

                    for dataClass in dataClassObj:
                        items.append(dataClass)

                        return items

                else:
                    dataClassObj = fromlist(dataClass, [parsedData])
                    return dataClassObj[0]

        except Exception as exception:
            raise Exception({"BaseFilterError": "Error trying to parse data"})
