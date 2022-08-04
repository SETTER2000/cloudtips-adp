from urllib.parse import urljoin
import requests
import json

from src.cloudtipsadp.constants import *


class Token:
    access_token: str
    expires_in: int
    token_type: str
    refresh_token: str
    scope: str


class CLoudTipsAdp:
    """Adapter class, helps client code interact with the service API."""
    refresh_token: str
    receivers: list = []
    headers = {}
    token = {}
    phoneNumber: str = '+79031012233'
    name: str = 'Иван'

    # def __init__(self, limit):
    #     self.records = []
    #     self.limit: int = limit
    #     # self.__today = dt.date.today()

    def get_token(self):
        """
        To start working with the API, you need to log in to the system,
        for this you need to get a login and password from your manager.
        :return: Token
        """
        data = {
            'Grant_type': 'password',
            'Client_id': 'Partner',
            'UserName': 'dmitriy.efremov@folovers.online',
            'Password': 'hw2ciQFwXQFej84'
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(
            AUTH_URL_SANDBOX, data=data, headers=headers)

        if response.ok:
            self.token: Token = response.json()
            return response
        return None

    def token_refresh(self):
        """
        To get a new access_token, you must use the refresh_token received
        during authorization. Get in return.
        :return: Token Update
        """
        pass

    @staticmethod
    def api(endpoint: str):
        """Вернёт правильный URL для запроса к API."""
        return urljoin(BASE_URL_API, endpoint)

    def create_many(self):
        """
        Для начала приема донатов вашими сотрудниками необходимо
        создать получателя в системе.
        :return:
        """
        data = {
            'placeId': CLOUDTIPS_ID_COMPANY,  # Идентификатор заведения
            'receivers': self.receivers,  # Список получателей
            'phoneNumber': self.phoneNumber,  # Номер получателя
            'name': self.name,  # Имя получателя
        }

        response = requests.post(
            self.api('receivers/create-many'),
            data=json.dumps(data),
            headers=self.headers)
        if response.ok:
            return response
        return None


if __name__ == '__main__':
    cta = CLoudTipsAdp()
    print(cta.get_token())
    print(cta.create_many())
