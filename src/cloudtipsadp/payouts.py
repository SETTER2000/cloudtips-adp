import requests
from src.cloudtipsadp.clients import Connect
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Payout:
    """Выплаты."""

    def __init__(self, payloads: dict = None):
        self.payload = payloads
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


class Payouts(Payout):
    """Выплаты."""
    base_path = 'payout'

    def __init__(self, payloads: dict = None):
        super(Payouts, self).__init__(payloads)

    def get(self):
        """Получение всех транзакций выплат получателям менеджера."""
        url = self(self.base_path)
        return self._get(url, self.payload)


if __name__ == '__main__':
    from core import Cloudtipsadp

    cta = Cloudtipsadp()
    cta.connect(sandbox=True)

    ob = cta.payouts_get(cta.payouts())

    if type(ob) == dict and ob.get('succeed'):
        print('Получение всех транзакций выплат получателям менеджера:')
        print(ob.get('data'))
    else:
        print(f'ERROR все: {ob}')
