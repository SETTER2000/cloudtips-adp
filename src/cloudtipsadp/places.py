import json
import os
import requests as requests

from src.cloudtipsadp.clients import Connect
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Place:
    """Заведения."""
    base_path = 'places'

    def __init__(self, user_id: str = None):
        self.user_id = user_id
        self.header = Connect.get_headers()

    def __call__(self, *args, **kwargs):
        return Connect.client.api(list(args))

    def _post(self, url, data: dict = dict()):
        return requests.post(url, data=json.dumps(data),
                             headers=self.header).json()

    def _get(self, url, params: dict = dict()):
        return requests.get(url, params=params, headers=self.header).json()

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
    def get_id():
        return os.getenv('placeId')

    def get(self):
        """Позволяет получить информацию по всем заведениям ТСП."""
        # URL для запроса к API
        url = self(self.base_path)
        return self._get(url)

    def send(self):
        """
        Привязка получателя к заведению.
        Отправить сотруднику на его номер телефона код в смс сообщении.
        """
        url = self(self.base_path, self.get_id(),
                   'employees', 'attach', 'send-sms')
        return self._post(url, dict(UserId=self.user_id))

    def confirm(self):
        """
        Подтвердить привязку телефона (пользователя) к предприятию.
        Передать код из смс.
        """
        url = self(
            self.base_path, self.get_id(), 'employees', 'attach', 'confirm')
        return self._post(url, dict(UserId=self.user_id, SmsCode=self.code))


if __name__ == '__main__':
    from core import Cloudtipsadp

    cta = Cloudtipsadp()
    cta.connect(sandbox=True)

    places = cta.places_send_sms(
        cta.places('44a38440-595d-494e-a028-09804355757a'))

    if places.get('succeed'):
        print(f'SMS отправлено: {places.get("data")}')
    else:
        print(places)

    # places = cta.places_confirm(
    #     cta.places('44a38440-595d-494e-a028-09804355757a', '000000'))
    #
    # if places.get('succeed'):
    #     print(f'Код из sms: '
    #           f'{places.get("data")}')
    # else:
    #     print(places)
    #
    # places = places_get(Places())
    # if places.get('succeed'):
    #     print(f'Получить информацию по всем заведениям ТСП: '
    #           f'{places.get("data")}')
    # else:
    #     print(places)
    #
