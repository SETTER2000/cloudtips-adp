import requests as requests

from cloudtipsadp.clients import Connect, SandboxClient
from cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Accumulation:
    """Карта."""
    base_path = 'accumulations'

    def __init__(self, user_id: str):
        self.user_id = user_id

    def get(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Accumulations(Accumulation):
    """Накопления."""

    def __init__(self, user_id):
        super(Accumulations, self).__init__(user_id)

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
    accumulations = Accumulations('19b3f83f-9930-4d50-b293-06edccbef2cf')
    # response = accum_get(accumulations)

    # if response.get('succeed'):
    #     print('Получить общую сумму донатов, по сотруднику:')
    #     print(response.get('data'))
    # else:
    #     print(response.get('errors'))
