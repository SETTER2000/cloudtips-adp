import requests as requests

from src.cloudtipsadp import Connect, SandboxClient
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Accumulation:
    """Карта."""
    base_path = 'accumulations'

    def __init__(self, user_id: str):
        self.user_id = user_id

    def get(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Accumulations(Accumulation):
    """Накопления."""

    def __init__(self, *args):
        super().__init__(*args)

    def get(self):
        """Получить общую сумму донатов, по сотруднику."""
        api_url = Connect.client.api([self.base_path, self.user_id, 'summary'])
        response = requests.get(api_url, headers=Connect.get_headers())
        return response.json()

    def payout(self):
        """Выплата накопления получателю."""
        # TODO CloudTips ещё не объявлены ручки
        pass


if __name__ == '__main__':
    connect = Connect(SandboxClient())
    ob = Accumulations('19b3f83f-9930-4d50-b293-06edccbef2cf').get()
    if ob.get('succeed'):
        print('Получить общую сумму донатов, по сотруднику:')
        print(ob.get('data'))
    else:
        print(ob.get('errors'))
