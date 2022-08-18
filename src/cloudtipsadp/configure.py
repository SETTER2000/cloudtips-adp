import os
from dotenv import load_dotenv
from dataclasses import dataclass
from loguru import logger

from src.cloudtipsadp.constants import (LOGS_NOT_LINK, CTA, LOGS_NOT_VALUES, )

load_dotenv()

level = 'DEBUG'


class ConfigurationError(Exception):
    pass


class DirLogs:
    __DIRS = {'root': ''}
    __file_name_log = 'cloudtipsadp.log'

    def __init__(self, path: str = None):
        self.path = path

    def __call__(self, *args, **kwargs):
        if self.path is not None:
            return os.path.join(self.__DIRS.get(self.path),
                                self.__file_name_log)
        return os.path.join(os.path.dirname(__file__), self.__file_name_log)


if os.getenv('LOG_LEVEL') is not None:
    level = DirLogs(os.getenv('LOG_LEVEL'))

path_log = DirLogs(os.getenv('LOG_OUT'))

try:
    logger.add(path_log(), format='{time} {level} {message}',
               level=level,
               rotation='5 MB', compression='zip')
except TypeError:
    print(f'{CTA}: {LOGS_NOT_VALUES}')


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
    pass
    # path_log = DirLogs(os.getenv('LOGS_OUT'))
    # print(f'path_log::: {path_log()}')
    # print(filters.__dict__)

    # level = os.getenv('LOG_LEVEL')
    # print(f'LOG-LLEVELL::: {level}')
    # print(f'path_log::: {path_log()}')
    #
    # print(os.getenv('LOGS_OUT'))
    # print(os.getenv('LOG_LEVEL'))
