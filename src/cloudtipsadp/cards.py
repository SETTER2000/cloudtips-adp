import json

import requests as requests

from src.cloudtipsadp.clients import Connect
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED, SITE_RETURNING_URL


class Card:
    """Карта."""
    base_path = 'cards'

    @classmethod
    def api_url(cls, *args):
        return Connect.client.api(list(args))

    def auth(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)

    def default(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)

    def delete(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)

    def get(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)

    def __init__(self, user_id: str = None):
        self.user_id = user_id


class Cards(Card):
    def __init__(self, user_id, key: str = None, token: str = None):
        super(Cards, self).__init__(user_id)
        self.checkout = key
        self.card_token = token

    def __get_data(self):
        try:
            data = dict(CardholderName='NONE',
                        CardCryptogramPacket=self.checkout,
                        UserId=self.user_id)
        except AttributeError:
            print('No user data.')
        else:
            return json.dumps(data)

    def auth(self):
        """Привязка карты получателю."""
        api_url = self.api_url(self.base_path, 'auth')
        parsed = requests.post(api_url, data=self.__get_data(),
                               headers=Connect.get_headers()).json()
        return parsed

    def get(self):
        """Список карт получателя."""
        api_url = self.api_url(self.base_path)
        parsed = requests.get(api_url, params=dict(userId=self.user_id),
                              headers=Connect.get_headers()).json()
        return parsed

    def default(self):
        """Изменить карту, на которую выплачиваются чаевые по умолчанию."""
        api_url = self.api_url(self.base_path, 'default')
        parsed = requests.post(
            api_url,
            data=json.dumps(dict(userId=self.user_id,
                                 cardToken=self.card_token)),
            headers=Connect.get_headers()).json()
        return parsed

    def delete(self):
        """Удаление карты получателя. Карту по умолчанию удалить нельзя."""
        api_url = self.api_url(self.base_path)
        parsed = requests.delete(
            api_url,
            data=json.dumps(dict(userId=self.user_id,
                                 cardToken=self.card_token)),
            headers=Connect.get_headers()).json()
        return parsed


class FlowBase:
    """Варианты авторизации карт."""

    def __init__(self, transactionId: int):
        self.transactionId = transactionId

    def auth(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Frictionless(FlowBase):
    """Карта не 3ds, либо получатель уже проходил авторизацию ранее."""

    def auth(self):
        pass


class Challenge(FlowBase):
    """Карта c 3ds и нужно подтверждение с вводом кода из sms."""

    def __init__(
            self,
            transactionId,
            md: str,
            paReq: str,
            acsUrl: str,
            statusCode: str,
            message: str = None,
            cardToken: str = None,
            issuerCode: str = None,
            otpRequired: str = None,
            cardIssuerBankCountry: str = None,
            cardLastFour: str = None,
            cardExpDate: str = None):
        super(Challenge, self).__init__(transactionId)
        self.md = md
        self.paReq = paReq
        self.acsUrl = acsUrl
        self.message = message
        self.statusCode = statusCode
        self.cardToken = cardToken
        self.issuerCode = issuerCode
        self.otpRequired = otpRequired
        self.cardIssuerBankCountry = cardIssuerBankCountry
        self.cardLastFour = cardLastFour
        self.cardExpDate = cardExpDate

    def __get_data(self):
        try:
            data = dict(MD=self.md,
                        PaReq=self.paReq,
                        TermUrl=SITE_RETURNING_URL)
        except AttributeError:
            print('No user data.')
        else:
            return json.dumps(data)

    def auth(self):
        """Авторизация платежа."""
        # api_url = self.api_url(self.base_path, 'auth')
        parsed = requests.post(self.acsUrl, data=self.__get_data()).json()
        return parsed


if __name__ == '__main__':
    from src.cloudtipsadp import Cloudtipsadp

    cta = Cloudtipsadp()
    cta.connect(sandbox=True)

    id = '23d3e83b-eef0-42dc-aa45-3d0b7e612924'
    checkout = ''

    ob = cta.cards_get(cta.cards('19b3f83f-9930-4d50-b293-06edccbef2cf'))
    if ob.get('succeed'):
        print('Список карт получателя:')
        print(ob.get('data'))
    else:
        print(ob.get('errors'))

    ob = cta.cards_auth(cta.cards(id, checkout))
    print(f'аутентификации:{ob}')

    ob = ob.get('data')
    print(f'PPPP:{ob}')

    if type(ob) == dict and len(ob) > 0:
        challenge = Challenge(**ob)
        print(challenge.__dict__)
        response = cta.cards_flow(challenge)

    # if (response.status_code != 204 and response.headers[
    #     "content-type"].strip().startswith("application/json")):
    #     try:
    #         print(f'3D Secure аутентификации:{response.json()}')
    #         # return response.json()
    #     except ValueError:
    #         # решить, как обращаться с сервером, который плохо себя ведет до
    #         #такой степени
    #         print('Error')
    # decide how to handle a server that's misbehaving to this extent

    # response.raise_for_status()  # raises exception when not a 2xx response
    # if response.status_code != 204:
    #     return response.json()
    # if ob.get('succeed'):
    #     print('Получить все карты привязанные получателем:')
    #     print(ob)
    # else:
    #     print(ob.get('errors'))

    # ob = card_get(Cards('19b3f83f-9930-4d50-b293-06edccbef2cf'))
