import json

import requests as requests

from src.cloudtipsadp.clients import Connect, SandboxClient
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Card:
    """Карта."""
    base_path = 'cards'

    def __init__(self, user_id: str = None):
        self.user_id = user_id

    def get(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Cards(Card):
    def __init__(self, user_id, checkout: str = None):
        super(Cards, self).__init__(user_id)
        self.checkout = checkout

    def get_data(self):
        try:
            data = dict(CardholderName='NONE',
                        CardCryptogramPacket=self.checkout,
                        UserId=self.user_id)
        except AttributeError:
            print('No user data.')
        else:
            return json.dumps(data)

    def get(self):
        """Список карт получателя."""
        # URL для запроса к API
        api_url = Connect.client.api([self.base_path])
        response = requests.get(api_url, params=dict(userId=self.user_id),
                                headers=Connect.get_headers())
        return response.json()

    def auth(self):
        """Привязка карты получателю."""
        api_url = Connect.client.api([self.base_path, 'auth'])
        response = requests.post(api_url, data=self.get_data(),
                                 headers=Connect.get_headers())
        return response.json()


def card_get(card: Card):
    return card.get()


if __name__ == '__main__':
    connect = Connect(SandboxClient())
    #
    ob = card_get(Cards('19b3f83f-9930-4d50-b293-06edccbef2cf'))
    if ob.get('succeed'):
        print('Список карт получателя:')
        print(ob.get('data'))
    else:
        print(ob.get('errors'))

    # ob = Cards('23d3e83b-eef0-42dc-aa45-3d0b7e612924',
    #            '014000003055241202aGxSPALEBgWhIpGZId98Jto0V8r/NLcFDZ+w9FqzXmwOLUdKah+M3DDeMW3yCj8ZA4O6YvGTMdt48azI1hmWYbbrhXgb4gQfrP1xcYG/jWG2sGvl+/EkIGc8r1QMaJI5QDfnqy5SFCnDt43mpJx/codgC1K2qkvmEfao+I74B4pKC/1hzouei4NDq8zDZ+6sWybkGXzGY4bFSeor07HLG9WMVGNus04jdn+k1rajgHQwGIkP44YcSN7iWVmY6xzysuZBq8AqiUxliMDNT9HMLFqZkZBFCZzu9QK5719+ELSRnfbJUKVPLwV2J3nLyl9WS+QK9PYILvModJ/CGx7BgA==')
    # ob = ob.auth()

    # ob = card_get(Cards('19b3f83f-9930-4d50-b293-06edccbef2cf'))
    # if ob.get('succeed'):
    #     print('Получить все карты привязанные получателем:')
    #     print(ob.get('data'))
    # else:
    #     print(ob.get('errors'))
