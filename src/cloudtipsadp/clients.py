import os
import traceback
from urllib.parse import urljoin
from configuration import Token
import requests as requests
from dotenv import load_dotenv

from constants import (BASE_URL, BASE_URL_API, BASE_URL_SANDBOX)

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


def my_name():
    """Получить имя текущего метода."""
    stack = traceback.extract_stack()
    print('Print from {}'.format(stack[-2][2]))


class BaseClient:
    token: Token
    base_url: str = BASE_URL
    headers: dict = {"Content-Type": "application/x-www-form-urlencoded"}
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
    def api(endpoint: str):
        """Вернёт правильный URL для запроса к API."""
        return urljoin(BASE_URL_API, endpoint)

    @classmethod
    def auth(cls):
        """Авторизоваться в системе."""
        return requests.post(cls.base_url, data=ConnectData.get(),
                             headers=cls.headers)

    def refresh_token(self):
        """
        Refresh token.
        Для получения нового access_token необходимо использовать
        refresh_token полученный при авторизации.
        """
        raise NotImplementedError('Base class method not implemented.')


class ProductClient(BaseClient):
    """Production server."""
    base_url = urljoin(BaseClient.base_url, BaseClient.auth_url)

    def refresh_token(self):
        return requests.post(self.base_url,
                             data=ConnectData.refresh(self.token),
                             headers=self.headers)


class SandboxClient(BaseClient):
    """Тестовый сервер. Для работы в песочнице."""
    base_url: str = urljoin(BASE_URL_SANDBOX, BaseClient.auth_url)

    def refresh_token(self):
        response = requests.post(self.base_url,
                                 data=ConnectData.refresh(self.token),
                                 headers=self.headers)
        self.valid(response)


class Connect:
    """Singleton."""
    __instance = None
    client = None

    def __new__(cls, client: BaseClient):
        if cls.__instance is None:
            cls.client = client
            cls.client.connect()
            cls.__instance = super(Connect, cls).__new__(cls)

        return cls.__instance

    @classmethod
    def get_token(cls):
        return (f'{cls.client.token["token_type"]}'
                f' {cls.client.token["access_token"]}')

    def refresh_token(self):
        self.client.refresh_token()
        return (f'{self.client.token["token_type"]}'
                f' {self.client.token["access_token"]}')


if __name__ == '__main__':
    # Чтоб понять как работает обновление и получение токенов,
    # нужно смотреть в дебагере. Run и Debug возвращают разные значения.
    # ProductClient - будет доступен с данными для production, когда менеджер
    # выдаст новые логин и пароль
    # client = ProductClient()
    connect = Connect(SandboxClient())
    connect2 = Connect(SandboxClient())
    token = connect.get_token()
    print(f'TOKEN::{token[-5:]}')

    refresh_token = connect.refresh_token()
    print(f'REFRESH TOKEN::{refresh_token[-5:]}')
    token2 = connect2.get_token()
    print(f'TOKEN2::{token2[-5:]}')

    refresh_token2 = connect.refresh_token()
    print(f'REFRESH TOKEN::{refresh_token2[-5:]}')
    token3 = connect2.get_token()

    print(f'TOKEN3::{token3[-5:]}')
    token2 = connect2.get_token()
    print(f'TOKEN2::{token2[-5:]}')
    token = connect.get_token()
    print(f'TOKEN::{token[-5:]}')
