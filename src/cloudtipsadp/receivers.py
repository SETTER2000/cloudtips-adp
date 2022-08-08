import json
import os

import requests as requests

from src.cloudtipsadp.clients import Connect, SandboxClient
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Receiver:
    receivers = list
    phone_number: str
    name: str
    place_id: str = str(os.getenv('placeId'))

    def __init__(self, name: str, phone_number: str):
        self.phone_number = phone_number
        self.name = name

    def get_data(self):
        try:
            receivers = [dict(phoneNumber=self.phone_number, name=self.name)]
            data = dict(placeId=self.place_id, receivers=receivers)
        except AttributeError:
            print('No user data.')
        else:
            return json.dumps(data)

    def create(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Receivers(Receiver):
    """Получатель донатов."""
    base_path = 'receivers'

    def __init__(self, *args):
        super().__init__(*args)

    def create(self):
        """Создать получателя донатов в сервисе."""
        # URL для запроса к API
        api_url = Connect.client.api([self.base_path, 'create-many'])
        response = requests.post(api_url, data=self.get_data(),
                                 headers=Connect.get_headers())
        if response.ok:
            return response.json()
        elif response.status_code == 415:
            connect.refresh_token()
            self.create()
        return None


if __name__ == '__main__':
    connect = Connect(SandboxClient())
    # connect.get_token()
    ob = Receivers("Olga", "+79105265720")
    if ob.create():
        print('Получатель создан.')
