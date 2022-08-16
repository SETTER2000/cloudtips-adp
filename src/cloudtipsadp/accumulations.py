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
        parsed = requests.get(api_url, headers=Connect.get_headers()).json()
        return parsed

    def __get_data(self):
        pass
        # try:
        #     receivers = [dict(phoneNumber=self.phone_number, name=self.name)]
        #     data = dict(placeId=Places.get_place(), receivers=receivers)
        # except AttributeError:
        #     print('No user data.')
        # else:
        #     return json.dumps(data)

    def payout_receiver(self):
        """Выплата накопления получателю."""
        # api_url = Connect.client.api([self.base_path, 'payout', self.user_id])
        # parsed = requests.post(api_url, data=self.__get_data(),
        #                        headers=Connect.get_headers()).json()
        # return parsed
        pass


if __name__ == '__main__':
    # connect = Connect(SandboxClient())
    # accumulations = Accumulations('19b3f83f-9930-4d50-b293-06edccbef2cf')
    # response = accum_get(accumulations)
    from core import Cloudtipsadp

    connect = Connect(SandboxClient())
    cta = Cloudtipsadp()

    ob = cta.accums_get(
        cta.accum(user_id='b8835022-f475-44b9-99d3-eddca9c3e44a'))
    if type(ob) == dict and ob.get('succeed'):
        print('Получить общую сумму донатов, по сотруднику:')
        print(ob.get('data'))
    else:
        print(f'ERROR все: {ob}')
