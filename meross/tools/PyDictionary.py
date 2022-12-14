from typing import Dict, Any


class PyDictionary:

    def __init__(self):
        self.dictionary: Dict = {}

    def Add(self, key: str, value: any) -> None:
        self.dictionary[key] = value

    def Get(self, key) -> Any:
        return self.dictionary.get(key)

    def Update(self, key, value) -> None:
        self.dictionary.update({key, value})

    def Delete(self, key) -> None:
        if self.Exist(key):
            del self.dictionary[key]

    def Exist(self, key) -> bool:
        return self.dictionary.get(key) is not None

    def Clone(self):
        pass
