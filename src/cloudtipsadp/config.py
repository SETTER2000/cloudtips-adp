from dataclasses import dataclass

from loguru import logger

logger.add("file_{time}.log", format='{time} {level} {message}', level='INFO',
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
