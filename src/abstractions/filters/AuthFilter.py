from dataclasses import dataclass
from .BaseFilters import BaseFilter
from ..auth import Auth


@dataclass
class AuthFilter(BaseFilter):

    credentials: Auth

    def __init__(self, data: str):
        if (data != None):
            self.credentials = super().__init__(data, Auth)
        else:
            self.credentials = None