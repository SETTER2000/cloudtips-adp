import json

import requests

from src.cloudtipsadp.connect.clients import Connect
from src.cloudtipsadp.connect.repository import Repository


class CardRepository(Repository):
    """Карта."""

    def __init__(self,
                 req: requests = None,
                 session: Connect = None,
                 base_path: str = None, ):
        super(CardRepository, self).__init__(req, session, base_path)

    def get(self, obj_id: str):
        """Список карт получателя."""
        url = self(self.base_path)
        parsed = self.req.get(url, params=dict(userId=obj_id),
                              headers=self.session.get_headers()).json()
        return parsed

    def list(self):
        pass

    def save(self, obj):
        pass

    def update(self, obj):
        pass

    def add(self, user_id, transact_id):
        """
        При успешном окончании методов 3, 4 или 5 необходимо подтвердить
        привязку карты на стороне системы.
        """
        url = self(self.base_path, 'add')
        return self.req.post(url, dict(
            userId=user_id, TransactionId=transact_id),
                             headers=self.session.get_headers()).json()

    def default(self, user_id, card_token):
        """Изменить карту, на которую выплачиваются чаевые по умолчанию."""
        url = self(self.base_path, 'default')
        return self.req.post(url, dict(
            userId=user_id, cardToken=card_token),
                             headers=self.session.get_headers()).json()

    def delete(self, user_id, card_token):
        """Удаление карты получателя. Карту по умолчанию удалить нельзя."""
        url = self(self.base_path)
        return self.req.delete(
            url, data=json.dumps(dict(userId=user_id, cardToken=card_token)),
            headers=self.session.get_headers()).json()

    def auth(self, user_id, checkout):
        """Привязка карты получателю."""
        url = self(self.base_path, 'auth')
        return self.req.post(url, json.dumps(
            dict(CardholderName='NONE', CardCryptogramPacket=checkout,
                 UserId=user_id)), headers=self.session.get_headers()).json()

    def post3ds(self, user_id, md, paRes):
        """Для проведения 3-D Secure аутентификации."""
        url = self(self.base_path, 'post3ds')
        return self.req.post(url, json.dumps(dict(userId=user_id, md=md,
                                                  paRes=paRes)),
                             headers=self.session.get_headers()).json()

    def get_token(self):
        """Return Header & Token."""
        return self.session.get_token()

    def refresh_token(self):
        """Return Refresh Token."""
        return self.session.refresh_token()
