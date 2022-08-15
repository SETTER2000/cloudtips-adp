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

    def pages(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Receivers(Receiver):
    """Получатель донатов."""
    base_path = 'receivers'

    def __init__(self, name: str = None, phone_number: str = None):
        super(Receivers, self).__init__(phone_number)
        self.name = name

    def __get_data(self):
        try:
            receivers = [dict(phoneNumber=self.phone_number, name=self.name)]
            data = dict(placeId=Places.get_place(), receivers=receivers)
        except AttributeError:
            print('No user data.')
        else:
            return json.dumps(data)

    def create(self):
        """Создать получателя донатов в сервисе."""
        api_url = Connect.client.api([self.base_path, 'create-many'])
        parsed = requests.post(api_url, data=self.__get_data(),
                               headers=Connect.get_headers()).json()
        return parsed

    def pages(self):
        """Все получатели в заведении."""
        api_url = Connect.client.api([self.base_path])
        parsed = requests.get(api_url, headers=Connect.get_headers()).json()
        return parsed


if __name__ == '__main__':
    from core import Cloudtipsadp

    connect = Connect(SandboxClient())
    cta = Cloudtipsadp()

    # ob = cta.receivers_pages(cta.receivers())
    # if ob.get('succeed'):
    #     print('Все получатели в системе:')
    #     print(ob.get('data'))
    # else:
    #     print(f'ERROR все: {ob}')

    # ob = cta.receivers_create(cta.receivers('Adam', '+79162047558'))
    # ob = cta.receivers_create(cta.receivers('Ozzy Osbourne', '+72002040001'))
    ob = cta.receivers_create(cta.receivers('AC/DC', '+71002040007'))
    print(ob)

    # Получатель уже есть в системе, но не в нашем скоупе.
    # ob = {'data': {'created': [{'phoneNumber': '+72002040005', 'name': 'Foo-55', 'userId': '21591c56-dfc6-432d-93af-882c0ea454aa', 'layoutId': 'a454aabd', 'layoutStatus': 'WaitingForConfirmation'}], 'skipped': []}, 'succeed': True, 'errors': None, 'validationErrors': None}

    # Новый получатель создан
    # ob = {'data': {'created': [{'phoneNumber': '+72002040005', 'name': 'Foo-55', 'userId': '21591c56-dfc6-432d-93af-882c0ea454aa', 'layoutId': 'a454aabd', 'layoutStatus': 'None'}], 'skipped': []}, 'succeed': True, 'errors': None, 'validationErrors': None}

    # Получатель уже есть в системе и находится в вашем скоупе,так как
    # находится в массиве skipped:
    # ob = {'data': {'created': [], 'skipped': [{'phoneNumber': '+79162047558', 'name': 'Adam', 'userId': '44a38440-595d-494e-a028-09804355757a', 'layoutId': '55757a3e', 'layoutStatus': 'None'}]}, 'succeed': True, 'errors': None, 'validationErrors': None}
    if ob.get('succeed'):
        if len(ob.get('data')['skipped']) > 0:
            print('Получатель уже есть в системе и находится в вашем скоупе,'
                  'так как находится в массиве skipped: ')
            print(ob.get('data')['skipped'])
        elif len(ob.get('data')['created']) > 0 and ob.get('data')['created'][0]['layoutStatus'] == 'WaitingForConfirmation':
            print('Получатель уже есть в системе, но не в нашем скоупе.')
            print('Так как есть в массиве created и '
                  'layoutStatus = WaitingForConfirmation:')
            print(ob.get('data')['created'])
            print('Получатель должен подтвердить свое желание, что вы его '
                  'привяжете к своему скоупу.')
            print('Для подтверждение, ему надо направить sms.')
        elif len(ob.get('data')['created']) > 0 and ob.get('data')['created'][0]['layoutStatus'] == 'None':
            print('Получатель не был в системе и сейчас был создан и '
                  'добавлен в ваш скоуп.')
            print(ob.get('data'))
        else:
            print(f'Получатель донатов создан.')
            print(ob.get('data'))

    else:
        print(f'ERROR: {ob}')

