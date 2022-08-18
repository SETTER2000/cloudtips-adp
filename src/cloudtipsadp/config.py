from dataclasses import dataclass

from loguru import logger

logger.add('debug.log', format='{time} {level} {message}', level='INFO',
           rotation='1 MB', compression='zip')


class ConfigurationError(Exception):
    pass


@dataclass(frozen=True)
class Token:
    access_token: str
    expires_in: int
    token_type: str
    refresh_token: str
    scope: str

    def refresh(self):
        return self.refresh_token


class Filter:
    dateFrom: str
    dateTo: str
    phoneNumber: str
    layoutId: str
    id: str
    status: str
    userId: str
    page: str
    limit: str

    def __init__(self, date_from: str = None,
                 date_to: str = None, phone: str = None,
                 layout_id: str = None, id: str = None, status: str = None,
                 user_id: str = None, page: str = None, limit: str = None):
        self.dateFrom = date_from
        self.dateTo = date_to
        self.phoneNumber = phone
        self.layoutId = layout_id
        self.id = id
        self.status = status
        self.userId = user_id
        self.page = page
        self.limit = limit


filters = Filter(date_from='2022-05-01',
                 date_to='2022-08-15',
                 phone='+79062047500')
if __name__ == '__main__':
    print(filters.__dict__)
