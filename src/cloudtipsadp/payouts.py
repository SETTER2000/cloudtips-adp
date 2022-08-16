import requests

from src.cloudtipsadp.clients import Connect, SandboxClient
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Payout:
    """Выплаты."""

    def get(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Payouts(Payout):
    """Выплаты."""
    base_path = 'receivers'

    def get(self):
        api_url = Connect.client.api([self.base_path])
        parsed = requests.get(api_url, headers=Connect.get_headers()).json()
        return parsed


if __name__ == '__main__':
    from core import Cloudtipsadp

    connect = Connect(SandboxClient())
    cta = Cloudtipsadp()

    ob = cta.payouts_get(cta.payouts())
    if type(ob) == dict and ob.get('succeed'):
        print('Получение всех транзакций выплат получателям менеджера:')
        print(ob.get('data'))
    else:
        print(f'ERROR все: {ob}')
