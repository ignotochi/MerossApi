import json
from typing import Optional

class BaseFilter():
    
    __parsedData = object()
    
    def __init__(self, data: str) -> None:
        if (data): self.ParseData(data)

    @classmethod
    def ParseData(self, data: str) -> None:
        self.__parsedData = json.loads(data) if len(json.loads(data)) != {} else None
        
    
    @classmethod
    def GetParsedData(self) -> object:
        return self.__parsedData



