from urllib.parse import urljoin

import requests as requests

from cloudtipsadp import constants as cnt
from cloudtipsadp import settings


class ConfigurationError(Exception):
    pass


class ConnectData:
    """
    Данные для подключения к API.
    Для начала работы с API вам необходимо авторизоваться в системе,
    для этого необходимо получить логин и пароль у вашего менеджера.
    Создайте файл .env в корне проекта и поместите туда (пример):

    Grant_type=password
    Client_id=Partner
    UserName=example@mail.ru
    Password=34tstg36t
    """

    @staticmethod
    def get():
        try:
            return dict(Client_id=settings.CTA_CLIENT_ID,
                        UserName=settings.CTA_USER_NAME,
                        Password=settings.CTA_PASSWORD,
                        Grant_type=settings.CTA_GRANT_TYPE)
        except AttributeError as e:
            raise SystemExit(e)

    @classmethod
    def refresh(cls, ref_token: settings.Token):
        return dict(Grant_type=settings.CTA_GRANT_TYPE_REFRESH,
                    Client_id=settings.CTA_CLIENT_ID,
                    refresh_token=ref_token['refresh_token'])


class BaseClient:
    token: settings.Token
    base_url = settings.BASE_URL
    auth_url = 'connect/token'

    def valid(self, response):
        if response.ok:
            self.token: settings.Token = response.json()
            return response
        return None

    def connect(self):
        response = self.auth()
        self.valid(response)

    @staticmethod
    def api(endpoints: list, base_url=settings.BASE_URL_API):
        """Вернёт правильный URL для запроса к API."""
        endpoints.insert(0, cnt.API_VERSION)
        path = '/'.join(x for x in endpoints)
        return urljoin(base_url, path)

    @classmethod
    def auth(cls):
        """Авторизоваться в системе."""
        data = ConnectData.get()
        return requests.post(cls.base_url, data=data,
                             headers=cnt.HEADERS_REQUEST)

    def refresh_token(self):
        """
        Refresh token.
        Для получения нового access_token необходимо использовать
        refresh_token полученный при авторизации.
        """
        raise NotImplementedError(cnt.M_BASE_IMPLEMENTED)


class CurrentClient(BaseClient):
    """Постоянный клиент сервера."""
    base_url: str = urljoin(settings.BASE_URL, BaseClient.auth_url)

    def refresh_token(self):
        response = requests.post(self.base_url,
                                 data=ConnectData.refresh(self.token),
                                 headers=cnt.HEADERS_REQUEST)
        self.valid(response)

    def api(self, endpoints: list, base_url=settings.BASE_URL_API):
        return super(CurrentClient, self).api(endpoints, base_url)


class Connect:
    """Singleton."""
    __instance = None
    client = None

    def __new__(cls, client: BaseClient = None):
        if cls.__instance is None:
            if client is None:
                cls.client = CurrentClient()
            else:
                cls.client = client

            cls.client.connect()
            cls.__instance = super(Connect, cls).__new__(cls)

        return cls.__instance

    @classmethod
    def get_token(cls):
        try:
            type_token = cls.client.token['token_type']
            access_token = cls.client.token['access_token']
            return f'{type_token} {access_token}'
        except AttributeError:
            print(cnt.CTA, cnt.BAD_CONNECT)

    def refresh_token(self):
        try:
            self.client.refresh_token()
        except AttributeError:
            print(cnt.CTA, cnt.BAD_CONNECT)
        else:
            type_token = self.client.token['token_type']
            access_token = self.client.token['access_token']
            return f'{type_token} {access_token}'

    @classmethod
    def get_headers(cls):
        return {'Authorization': f'{cls.get_token()}',
                'Content-Type': 'application/json'}

    @classmethod
    def get_headers_token(cls):
        return {'Authorization': f'{cls.get_token()}'}
