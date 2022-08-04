import os
import traceback
from urllib.parse import urljoin

import requests as requests
from dotenv import load_dotenv

from src.cloudtipsadp.constants import (
    BASE_URL, BASE_URL_SANDBOX, BASE_URL_API)

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


class Token:
    access_token: str
    expires_in: int
    token_type: str
    refresh_token: str
    scope: str


def my_name():
    """Получить имя текущего метода."""
    stack = traceback.extract_stack()
    print('Print from {}'.format(stack[-2][2]))


class BaseClient:
    token: Token
    base_url: str = BASE_URL
    headers: dict = {"Content-Type": "application/x-www-form-urlencoded"}

    def connect(self):
        raise NotImplementedError()

    @staticmethod
    def api(endpoint: str):
        """Вернёт правильный URL для запроса к API."""
        return urljoin(BASE_URL_API, endpoint)

    # def get_token(self, result):
    #     if result.ok:
    #         self.token: Token = result.json()
    #         return result
    #     return None

    # def get(self):
    #     raise NotImplementedError(f'The {my_name()} method is not '
    #                               f'implemented in the child class')

    # def __call__(self, *args, **kwargs):
    #     return self.make_get_request()


class ProductClient(BaseClient):
    """Production server."""
    base_url = urljoin(BaseClient.base_url, 'connect/token')

    def connect(self):
        response = requests.post(self.base_url, data=ConnectData.get(),
                                 headers=self.headers)
        if response.ok:
            self.token: Token = response.json()
            return response
        return None


class SandboxClient(BaseClient):
    """Для работы в песочнице. Тестовый сервер."""
    base_url: str = urljoin(BASE_URL_SANDBOX, 'connect/token')

    def connect(self):
        response = requests.post(self.base_url, data=ConnectData.get(),
                                 headers=self.headers)
        if response.ok:
            self.token: Token = response.json()
            return response
        return None


def connect(cl: BaseClient):
    contact = cl.connect()
    print(f'CONNECT: {contact}')


if __name__ == '__main__':
    # ProductClient - будет доступен с данными для продакшен, когда менеджер
    # выдаст новые логин и пароль
    # client = ProductClient()
    connect(SandboxClient())
