import os
import traceback
from urllib.parse import urljoin
from .configuration import Token
import requests as requests
from dotenv import load_dotenv

from .constants import BASE_URL, BASE_URL_API, BASE_URL_SANDBOX, BASE_URL_API_SANDBOX

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


def my_name():
    """Получить имя текущего метода."""
    stack = traceback.extract_stack()
    print('Print from {}'.format(stack[-2][2]))


class BaseClient:
    token: Token
    base_url: str = BASE_URL
    headers: dict = {"Content-Type": "application/x-www-form-urlencoded"}
    auth_url = 'connect/token'

    # def auth(self):
    #     """Получить объект Response от сервиса CloudTips."""
    #     raise NotImplementedError()

    def connect(self):
        response = self.auth()
        if response.ok:
            self.token: Token = response.json()
            return response
        return None

    @staticmethod
    def api(endpoint: str):
        """Вернёт правильный URL для запроса к API."""
        return urljoin(BASE_URL_API, endpoint)

    @classmethod
    def auth(cls):
        return requests.post(cls.base_url, data=ConnectData.get(),
                             headers=cls.headers)


class ProductClient(BaseClient):
    """Production server."""
    base_url = urljoin(BaseClient.base_url, BaseClient.auth_url)
    BaseClient.auth()


class SandboxClient(BaseClient):
    """Для работы в песочнице. Тестовый сервер."""
    base_url: str = urljoin(BASE_URL_SANDBOX, BaseClient.auth_url)
    BaseClient.auth()


class Connect:
    def __init__(self, client: BaseClient):
        self.client = client()
        self.client.connect()

    def get_token(self):
        return (f'{self.client.token["token_type"]}'
                f' {self.client.token["access_token"]}')


if __name__ == '__main__':
    # ProductClient - будет доступен с данными для продакшен, когда менеджер
    # выдаст новые логин и пароль
    # client = ProductClient()
    Connect(SandboxClient())
