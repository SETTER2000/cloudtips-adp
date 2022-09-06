__all__ = [
    'BAD_CONNECT',
    'BASE_IMPLEMENTED',
    'API_VERSION',
    'HEADERS_REQUEST',
    'SITE_RETURNING_URL',
    'FILE_PATH_BAD',
    'CTA',
    'JSON_ERR_OBJECT',
]
CTA = 'cloudtipsadp: '
BAD_CONNECT = 'Ошибка. Не могу подключиться к cloudtips.'
BASE_IMPLEMENTED = 'Base class method not implemented.'
# URL для приема ответа от платежной системы при привязке карты
SITE_RETURNING_URL = 'http://127.0.0.1:8000'
API_VERSION = 'api'
FILE_PATH_BAD = 'File path missing:'
HEADERS_REQUEST = {"Content-Type": "application/x-www-form-urlencoded"}
JSON_ERR_OBJECT = 'Ошибка получения значения от сервиса.'
