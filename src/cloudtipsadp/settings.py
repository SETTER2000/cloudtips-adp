import os
from dataclasses import dataclass

BASE_URL = os.environ.get('CTA_BASE_URL')
BASE_URL_API = os.environ.get('CTA_BASE_URL_API')

CTA_CLIENT_ID = os.environ.get('CTA_CLIENT_ID', 'Partner')
CTA_USER_NAME = os.environ.get('CTA_USER_NAME')
CTA_PASSWORD = os.environ.get('CTA_PASSWORD')
CTA_GRANT_TYPE = os.environ.get('CTA_GRANT_TYPE', 'password')
CTA_GRANT_TYPE_REFRESH = 'refresh_token'
CTA_PLACE_ID = os.environ.get('CTA_PLACE_ID')


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
