from meross.abstractions.webFilters.base.BaseFilters import BaseFilter
from meross.abstractions.auth.auth import Auth


class AuthFilter(BaseFilter):

    def __init__(self, data: bytes):

        self.credentials: Auth

        super(AuthFilter, self).__init__(data, Auth)
        self.credentials = self._parsedData

    def Reset(self) -> None:
        del self.credentials
