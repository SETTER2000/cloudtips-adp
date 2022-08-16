import json
import os
import requests as requests

from cloudtipsadp.clients import Connect, SandboxClient
from cloudtipsadp.constants import M_BASE_IMPLEMENTED


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
        parsed = requests.get(api_url, headers=Connect.get_headers()).json()
        return parsed

    def send(self):
        """
        Привязка получателя к заведению.
        Отправить сотруднику на его номер телефона код в смс сообщении.
        """
        api_url = Connect.client.api(
            [self.base_path, self.get_place(), 'employees', 'attach',
             'send-sms'])
        parsed = requests.post(
            api_url, data=json.dumps(dict(UserId=self.user_id)),
            headers=Connect.get_headers()).json()
        return parsed

    def confirm(self):
        """
        Подтверждение привязки телефона (пользователя) к предприятию.
        Передать код из смс.
        """
        api_url = Connect.client.api(
            [self.base_path, self.get_place(), 'employees', 'attach',
             'confirm'])
        parsed = requests.post(
            api_url, data=json.dumps(dict(UserId=self.user_id,
                                          SmsCode=self.code)),
            headers=Connect.get_headers()).json()
        return parsed


if __name__ == '__main__':
    from core import Cloudtipsadp
    connect = Connect(SandboxClient())
    cta = Cloudtipsadp()

    places = cta.places_send_sms(
        cta.places('44a38440-595d-494e-a028-09804355757a'))

    if places.get('succeed'):
        print(f'SMS отправлено: {places.get("data")}')
    else:
        print(places)

    places = cta.places_confirm(
        cta.places('44a38440-595d-494e-a028-09804355757a', '000000'))

    if places.get('succeed'):
        print(f'Код из sms: '
              f'{places.get("data")}')
    else:
        print(places)
    #
    # places = places_get(Places())
    # if places.get('succeed'):
    #     print(f'Получить информацию по всем заведениям ТСП: '
    #           f'{places.get("data")}')
    # else:
    #     print(places)
    #
