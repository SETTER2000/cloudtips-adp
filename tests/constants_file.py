__all__ = [
    'BASE_URL',
    'BASE_URL_API',
    'BASE_URL_SANDBOX',
    'BASE_URL_API_SANDBOX',
    'M_BAD_CONNECT',
    'M_BASE_IMPLEMENTED',
    'API_VERSION',
    'HEADERS_REQUEST',
    'SITE_RETURNING_URL',
]
BASE_URL = 'https://identity.cloudtips.ru'
BASE_URL_SANDBOX = 'https://identity-sandbox.cloudtips.ru'
BASE_URL_API = 'https://api.cloudtips.ru/api'
BASE_URL_API_SANDBOX = 'https://api-sandbox.cloudtips.ru'
M_BAD_CONNECT = 'No service connection.'
M_BASE_IMPLEMENTED = 'Base class method not implemented.'
# URL сайта для возврата плательщика после аутентификации карты
SITE_RETURNING_URL = 'http://127.0.0.1:8000'
API_VERSION = 'api'
HEADERS_REQUEST = {"Content-Type": "application/x-www-form-urlencoded"}
