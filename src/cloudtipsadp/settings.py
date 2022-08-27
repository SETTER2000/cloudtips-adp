import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('CTA_BASE_URL')
BASE_URL_API = os.getenv('CTA_BASE_URL_API')

CTA_CLIENT_ID = os.getenv('CTA_CLIENT_ID')
CTA_USER_NAME = os.getenv('CTA_USER_NAME')
CTA_PASSWORD = os.getenv('CTA_PASSWORD')
CTA_GRANT_TYPE = os.getenv('CTA_GRANT_TYPE')
CTA_GRANT_TYPE_REFRESH = 'refresh_token'
CTA_PLACE_ID = os.getenv('CTA_PLACE_ID')


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
