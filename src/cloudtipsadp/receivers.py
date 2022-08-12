import json

import requests as requests

from src.cloudtipsadp.places import Places
from src.cloudtipsadp.clients import Connect, SandboxClient
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Receiver:
    receivers = list
    phone_number: str
    name: str

    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def create(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Receivers(Receiver):
    """Получатель донатов."""
    base_path = 'receivers'

    def __init__(self, name: str, phone_number: str):
        super(Receivers, self).__init__(phone_number)
        self.name = name

    def get_data(self):
        try:
            receivers = [dict(phoneNumber=self.phone_number, name=self.name)]
            data = dict(placeId=Places.get_place(), receivers=receivers)
        except AttributeError:
            print('No user data.')
        else:
            return json.dumps(data)

    def create(self):
        """Создать получателя донатов в сервисе."""
        # URL для запроса к API
        api_url = Connect.client.api([self.base_path, 'create-many'])
        response = requests.post(api_url, data=self.get_data(),
                                 headers=Connect.get_headers())
        return response.json()


if __name__ == '__main__':
    connect = Connect(SandboxClient())
    # connect.get_token()
    ob = receiver_create(Receivers('Adam', '+79162047558'))
    if ob.get('succeed'):
        print(f'Получатель создан. {ob}')
