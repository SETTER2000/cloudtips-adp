import json
import os
import requests as requests

from src.cloudtipsadp.clients import Connect, SandboxClient
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Place:
    """Заведения."""
    base_path = 'places'

    def __init__(self, user_id: str = None):
        self.user_id = user_id

    def get(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)

    def send(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)

    def confirm(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Places(Place):
    def __init__(self, user_id: str = None, code: str = None):
        super(Places, self).__init__(user_id)
        self.code = code

    @staticmethod
    def get_place():
        return os.getenv('placeId')

    def get(self):
        """Позволяет получить информацию по всем заведениям ТСП."""
        # URL для запроса к API
        api_url = Connect.client.api([self.base_path])
        response = requests.get(api_url, headers=Connect.get_headers())
        return response.json()

    def send(self):
        """
        Привязка получателя к заведению.
        Отправить сотруднику на его номер телефона код в смс сообщении.
        """
        api_url = Connect.client.api(
            [self.base_path, self.get_place(), 'employees', 'attach',
             'send-sms'])
        response = requests.post(
            api_url, data=json.dumps(dict(UserId=self.user_id)),
            headers=Connect.get_headers())
        return response.json()

    def confirm(self):
        """
        Подтверждение привязки телефона (пользователя) к предприятию.
        Передать код из смс.
        """
        api_url = Connect.client.api(
            [self.base_path, self.get_place(), 'employees', 'attach',
             'confirm'])
        response = requests.post(
            api_url, data=json.dumps(dict(UserId=self.user_id,
                                          SmsCode=self.code)),
            headers=Connect.get_headers())
        return response.json()


if __name__ == '__main__':
    connect = Connect(SandboxClient())
    # places = place_send(Places('19b3f83f-9930-4d50-b293-06edccbef2cf'))
    # if places.get('succeed'):
    #     print(f'SMS отправлено: {places.get("data")}')
    # else:
    #     print(places)
    # #
    #
    # places = places_get(Places())
    # if places.get('succeed'):
    #     print(f'Получить информацию по всем заведениям ТСП: '
    #           f'{places.get("data")}')
    # else:
    #     print(places)
    #
    # places = places_confirm(Places('19b3f83f-9930-4d50-b293-06edccbef2cf',
    #                               '123456'))
    # if places.get('succeed'):
    #     print(f'Получить информацию по всем заведениям ТСП: '
    #           f'{places.get("data")}')
    # else:
    #     print(places)
