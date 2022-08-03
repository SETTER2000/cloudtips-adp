from urllib.parse import urljoin
import requests
import json

from constants import *

TODOS_URL = urljoin(BASE_URL, 'todos')


class CLoudTipsAdp:
    """Adapter class, helps client code interact with the service API."""
    refresh_token: str

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
        # headers = {}
        response = requests.post(
            AUTH_URL, data=json.dumps(data), headers=headers)
        if response.ok:
            return response
        return None

    def token_refresh(self):
        """
        To get a new access_token, you must use the refresh_token received
        during authorization. Get in return.
        :return: Token Update
        """
        pass


if __name__ == '__main__':
    cta = CLoudTipsAdp()
    print(cta.get_token())
