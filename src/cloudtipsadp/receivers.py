import json
import magic
import os
import requests

from src.cloudtipsadp.places import Places
from src.cloudtipsadp.clients import Connect
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED, FILE_PATH_BAD

mime = magic.Magic(mime=True)


class Receiver:
    receivers = list
    phone_number: str
    name: str

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.header = Connect.get_headers()

    def __call__(self, *args, **kwargs):
        return Connect.client.api(list(args))

    def _post(self, url, data: dict = dict()):
        return requests.post(url, data=json.dumps(data),
                             headers=self.header).json()

    def _get(self, url, params: dict = dict()):
        return requests.get(url, params=params, headers=self.header).json()

    def create(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)

    def pages(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)

    def photo(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)

    def detach_agent(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Receivers(Receiver):
    """Получатель донатов."""
    base_path = 'receivers'

    def __init__(self, name: str = None, phone_number: str = None,
                 user_id: str = None, photo_path: str = None):
        super(Receivers, self).__init__(phone_number)
        self.name = name
        self.user_id = user_id
        self.photo_path = photo_path

    def __get_data(self):
        try:
            receivers = [dict(phoneNumber=self.phone_number, name=self.name)]
            data = dict(placeId=Places.get_id(), receivers=receivers)
        except AttributeError:
            print('No user data.')
        else:
            return data

    def create(self):
        """Создать получателя донатов в сервисе."""
        url = self(self.base_path, 'create-many')
        return self._post(url, self.__get_data())

    def detach_agent(self):
        """Удалить получателя из скоупа."""
        try:
            url = self(self.base_path, self.user_id, 'detach-agent')
            parsed = self._post(url)
        except TypeError:
            print('NotFound user_id.')
        else:
            return parsed

    def pages(self):
        """Все получатели в заведении."""
        api_url = self(self.base_path)
        return self._get(api_url)

    def filter(self, ):
        """Выборка данных согласно параметрам запроса."""
        pass

    def photo(self):
        """Загрузить фотографию получателя."""
        payload = {}
        try:
            paths = os.path.split(self.photo_path)
            files = [
                ('FormFile', (
                    paths[1],
                    open(self.photo_path, 'rb'),
                    magic.from_file(self.photo_path, mime=True)))]
        except TypeError:
            print(f'{FILE_PATH_BAD}')
        except FileNotFoundError as e:
            print(f'{FILE_PATH_BAD} {e}')
        else:
            url = self(self.base_path, self.user_id, 'photo')
            parsed = requests.post(
                url, headers=Connect.get_headers_token(), data=payload,
                files=files).json()
            return parsed


if __name__ == '__main__':
    from core import Cloudtipsadp

    cta = Cloudtipsadp()
    cta.connect(sandbox=True)
    # user_id = '44a38440-595d-494e-a028-09804355757a'

    name = 'Poale Ell Adam'
    phone_number = '+79162047558'
    response = cta.receivers_create(cta.receivers(name, phone_number))
    if type(response) == dict and response.get('succeed'):
        print('Получатель донатов создан:')
        print(response.get('data'))
        # obg = response.get('data')
        # print(obg)
        user_id = response.get('data')['created'][0]['userId']
        print(f'USER ID: {user_id}')
    else:
        print(f'ERROR**: {response}')

    response = cta.places_send_sms(cta.places(user_id=user_id))
    if type(response) == dict and response.get('succeed'):
        print(
            f'Отправлено сообщении код в смс на телефон получателя {user_id}')
        print(response)
        response = cta.places_confirm(cta.places(user_id=user_id, code=000000))
        if type(response) == dict and response.get('succeed'):
            print(
                f'Отправлен код из SMS получателя: {user_id}')
            print(response)
        else:
            print(f'ERROR код: {response}')
    else:
        print(f'ERROR все: {response}')

    # user_id = '44a38440-595d-494e-a028-09804355757a'
    response = cta.receivers_detach_agent(cta.receivers(user_id=user_id))
    if type(response) == dict and response.get('succeed'):
        print(f'Удалён получатель {user_id} из скоупа:')
        print(response)
    else:
        print(f'ERROR все: {response}')

    response = cta.receivers_pages(cta.receivers())
    if type(response) == dict and response.get('succeed'):
        print('Все получатели донатов:')
        print(response.get('data'))
    else:
        print(f'ERROR donations: {response}')
    # photo_path = '/home/setter/Изображения/Рецепты/1.png'
    # response = cta.receivers_photo(cta.receivers(user_id=user_id,
    #                                        photo_path=photo_path))
    # if type(response) == dict and response.get('succeed'):
    #     print('Фото получателя успешно загружено:')
    #     print(response.get('data'))
    # else:
    #     print(f'ERROR все: {response}')

    # response = cta.receivers_pages(cta.receivers())
    # if response.get('succeed'):
    #     print('Все получатели в системе:')
    #     print(response.get('data'))
    # else:
    #     print(f'ERROR все: {response}')

    # response = cta.receivers_create(cta.receivers('Adam', '+79162047558'))
    # response = cta.receivers_create(cta.receivers('Ozzy Osbourne', '+72002040001'))
    # response = cta.receivers_create(cta.receivers('AC/DC', '+71002040007'))
    # print(response)

    # Получатель уже есть в системе, но не в нашем скоупе.
    # response = {'data': {'created': [{'phoneNumber': '+72002040005',
    # 'name': 'Foo-55', 'userId': '21591c56-dfc6-432d-93af-882c0ea454aa',
    # 'layoutId': 'a454aabd', 'layoutStatus': 'WaitingForConfirmation'}],
    # 'skipped': []}, 'succeed': True, 'errors': None,
    # 'validationErrors': None}

    # Новый получатель создан
    # response = {'data': {'created': [{'phoneNumber': '+72002040005',
    # 'name': 'Foo-55', 'userId': '21591c56-dfc6-432d-93af-882c0ea454aa',
    # 'layoutId': 'a454aabd', 'layoutStatus': 'None'}], 'skipped': []},
    # 'succeed': True, 'errors': None, 'validationErrors': None}

    # Получатель уже есть в системе и находится в вашем скоупе,так как
    # находится в массиве skipped:
    # response = {'data': {'created': [], 'skipped': [{'phoneNumber': '+79162047558',
    # 'name': 'Adam', 'userId': '44a38440-595d-494e-a028-09804355757a',
    # 'layoutId': '55757a3e', 'layoutStatus': 'None'}]}, 'succeed': True,
    # 'errors': None, 'validationErrors': None}

    # if response.get('succeed'):
    #     if len(response.get('data')['skipped']) > 0:
    #         print('Получатель уже есть в системе и находится в вашем скоупе,'
    #               'так как находится в массиве skipped: ')
    #         print(response.get('data')['skipped'])
    #     elif len(response.get('data')['created']) > 0 and \
    #             response.get('data')['created'][0][
    #                 'layoutStatus'] == 'WaitingForConfirmation':
    #         print('Получатель уже есть в системе, но не в нашем скоупе.')
    #         print('Так как есть в массиве created и '
    #               'layoutStatus = WaitingForConfirmation:')
    #         print(response.get('data')['created'])
    #         print('Получатель должен подтвердить свое желание, что вы его '
    #               'привяжете к своему скоупу.')
    #         print('Для подтверждение, ему надо направить sms.')
    #     elif len(response.get('data')['created']) > 0 and \
    #             response.get('data')['created'][0]['layoutStatus'] == 'None':
    #         print('Получатель не был в системе и сейчас был создан и '
    #               'добавлен в ваш скоуп.')
    #         print(response.get('data'))
    #     else:
    #         print(f'Получатель донатов создан.')
    #         print(response.get('data'))
    # else:
    #     print(f'ERROR: {response}')
