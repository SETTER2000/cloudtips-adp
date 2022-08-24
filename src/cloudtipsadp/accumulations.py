import requests as requests

from src.cloudtipsadp.clients import Connect
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Accumulation:
    """Карта."""
    base_path = 'accumulations'

    def __init__(self, user_id: str):
        self.user_id = user_id

    def __call__(self, *args, **kwargs):
        return Connect.client.api(list(args))

    def get(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Accumulations(Accumulation):
    """Накопления."""

    def __init__(self, user_id):
        super(Accumulations, self).__init__(user_id)

    def get(self):
        """Получить общую сумму донатов, по сотруднику."""
        api_url = self(self.base_path, self.user_id, 'summary')
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
        # api_url = self(self.base_path, 'payout', self.user_id)
        # parsed = requests.post(api_url, data=self.__get_data(),
        #                        headers=Connect.get_headers()).json()
        # return parsed
        pass


if __name__ == '__main__':
    from src.cloudtipsadp import Cloudtipsadp

    cta = Cloudtipsadp()
    cta.connect(sandbox=True)

    # accumulations = Accumulations('19b3f83f-9930-4d50-b293-06edccbef2cf')
    # response = accum_get(accumulations)

    ob = cta.accums_get(
        cta.accums(user_id='44a38440-595d-494e-a028-09804355757a'))
    if type(ob) == dict and ob.get('succeed'):
        print('Получить общую сумму донатов, по сотруднику:')
        print(ob.get('data'))
    else:
        print(f'ERROR все: {ob}')
