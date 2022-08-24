import json

import requests as requests

from src.cloudtipsadp.clients import Connect
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Accumulation:
    """Карта."""
    base_path = 'accumulations'

    def __init__(self, user_id: str):
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


class Accumulations(Accumulation):
    """Накопления."""

    def __init__(self, user_id):
        super(Accumulations, self).__init__(user_id)

    def summary(self):
        """Накопления получателя."""
        url = self(self.base_path, self.user_id, 'summary')
        return self._get(url)

    def payout_receiver(self):
        """Выплата накопления получателю."""
        url = self(self.base_path, 'payout', self.user_id)
        return self._post(url)


if __name__ == '__main__':
    from src.cloudtipsadp import Cloudtipsadp

    cta = Cloudtipsadp()
    cta.connect(sandbox=True)

    # accumulations = Accumulations('19b3f83f-9930-4d50-b293-06edccbef2cf')
    # response = accum_get(accumulations)

    response = cta.accums_summary(
        cta.accums(user_id='44a38440-595d-494e-a028-09804355757a'))
    if type(response) == dict and response.get('succeed'):
        print('Получить общую сумму донатов, по сотруднику:')
        print(response.get('data'))
    else:
        print(f'ERROR все: {response}')

    response = cta.accums_payout_receiver(
        cta.accums(user_id='44a38440-595d-494e-a028-09804355757a'))
    if type(response) == dict and response.get('succeed'):
        print('Выплата накопления получателю:')
        print(response.get('data'))
    else:
        print(f'ERROR все: {response}')
