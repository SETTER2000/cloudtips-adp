import os
from urllib.parse import urljoin

import requests as requests
from dotenv import load_dotenv

from cloudtipsadp.config import Token
from cloudtipsadp.constants import (API_VERSION, BASE_URL, BASE_URL_API,
                                        BASE_URL_API_SANDBOX, BASE_URL_SANDBOX,
                                        HEADERS_REQUEST, M_BAD_CONNECT,
                                        M_BASE_IMPLEMENTED)

load_dotenv()


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
        return dict(Client_id=os.getenv('Client_id'),
                    UserName=os.getenv('UserName'),
                    Password=os.getenv('Password'),
                    Grant_type=os.getenv('Grant_type'))

    @classmethod
    def refresh(cls, tkn: Token):
        return dict(Grant_type='refresh_token',
                    Client_id=os.getenv('Client_id'),
                    refresh_token=tkn['refresh_token'])


class BaseClient:
    token: Token
    base_url: str = BASE_URL
    auth_url = 'connect/token'

    def valid(self, response):
        if response.ok:
            self.token: Token = response.json()
            return response
        return None

    def connect(self):
        response = self.auth()
        self.valid(response)

    @staticmethod
    def api(endpoints: list, base_url=BASE_URL_API):
        """Вернёт правильный URL для запроса к API."""
        endpoints.insert(0, API_VERSION)
        path = '/'.join(x for x in endpoints)
        return urljoin(base_url, path)

    @classmethod
    def auth(cls):
        """Авторизоваться в системе."""
        return requests.post(cls.base_url, data=ConnectData.get(),
                             headers=HEADERS_REQUEST)

    def refresh_token(self):
        """
        Refresh token.
        Для получения нового access_token необходимо использовать
        refresh_token полученный при авторизации.
        """
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class ProductClient(BaseClient):
    """Production server."""
    base_url = urljoin(BaseClient.base_url, BaseClient.auth_url)

    def refresh_token(self):
        return requests.post(self.base_url,
                             data=ConnectData.refresh(self.token),
                             headers=HEADERS_REQUEST)

    @staticmethod
    def api(endpoints: list, base_url=BASE_URL_API):
        pass


class SandboxClient(BaseClient):
    """Тестовый сервер. Для работы в песочнице."""
    base_url: str = urljoin(BASE_URL_SANDBOX, BaseClient.auth_url)

    def refresh_token(self):
        response = requests.post(self.base_url,
                                 data=ConnectData.refresh(self.token),
                                 headers=HEADERS_REQUEST)
        self.valid(response)

    def api(self, endpoints: list, base_url=BASE_URL_API_SANDBOX):
        return super(SandboxClient, self).api(endpoints, base_url)


class Connect:
    """Singleton."""
    __instance = None
    client = None

    def __new__(cls, client: BaseClient = None):
        if cls.__instance is None:
            if client is None:
                cls.client = ProductClient()
            else:
                cls.client = client

            cls.client.connect()
            cls.__instance = super(Connect, cls).__new__(cls)

        return cls.__instance

    @classmethod
    def get_token(cls):
        # TODO заменить на метод get() ["token.."] и т.п. Избавиться от
        #  двойных кавычек и желтизны кода.

        try:
            type_token = cls.client.token['token_type']
            access_token = cls.client.token['access_token']
            return f'{type_token} {access_token}'
        except AttributeError:
            print(M_BAD_CONNECT)

    def refresh_token(self):
        try:
            self.client.refresh_token()
        except AttributeError:
            print(M_BAD_CONNECT)
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


if __name__ == '__main__':
    # Чтоб понять как работает обновление и получение токенов,
    # нужно смотреть в дебагере. Run и Debug возвращают разные значения.
    # ProductClient - будет доступен с данными для production, когда менеджер
    # выдаст новые логин и пароль
    # Подключение к Production service
    # connect = Connect()
    # # Получить токен
    # token = connect.get_token()

    # Подключение к Sandbox service
    connect = Connect(SandboxClient())
    # Получить токен
    token = connect.get_token()
    print(token)
    #
    # token = connect.refresh_token()
    # print(token)
