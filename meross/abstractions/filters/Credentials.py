from meross.abstractions.filters.BaseFilters import BaseFilter
from meross.abstractions.auth import Auth


class Credentials(BaseFilter):

    def __init__(self, data: bytes):

        self.credentials: Auth
        super(Credentials, self).__init__(data, Auth)

        self.credentials = self._parsedData

    def Reset(self) -> None:
        del self.credentials