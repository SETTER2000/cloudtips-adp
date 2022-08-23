import requests
from src.cloudtipsadp.clients import Connect
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Payout:
    """Выплаты."""

    def __init__(self, payloads: dict = None):
        self.payload = payloads

    @classmethod
    def api_url(cls, *args):
        return Connect.client.api(list(args))

    def get(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Payouts(Payout):
    """Выплаты."""
    base_path = 'payout'

    def __init__(self, payloads: dict = None):
        super(Payouts, self).__init__(payloads)

    def get(self):
        """Получение всех транзакций выплат получателям менеджера."""
        api_url = self.api_url(self.base_path)
        parsed = requests.get(
            api_url, params=self.payload, headers=Connect.get_headers()).json()
        return parsed


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
