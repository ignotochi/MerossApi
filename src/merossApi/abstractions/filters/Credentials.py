from dataclasses import dataclass
from merossApi.abstractions.filters.BaseFilters import BaseFilter
from merossApi.abstractions.auth import Auth


@dataclass
class Credentials(BaseFilter):

    def __init__(self, data: str):
        self.credentials: Auth
        
        if (data != None):
            self.credentials = super().__init__(data, Auth)

    def Reset(self) -> None:
        del self.credentials
