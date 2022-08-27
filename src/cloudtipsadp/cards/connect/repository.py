import json
import requests

from src.cloudtipsadp.connect.clients import Connect
from src.cloudtipsadp.connect.repository import Repository
from src.cloudtipsadp.constants import FILE_PATH_BAD
from src.cloudtipsadp.settings import CTA_PLACE_ID


class CardRepository(Repository):
    """Заведения."""

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

    #     """Позволяет получить информацию по всем заведениям ТСП."""
    #     api_url = self(self.base_path)
    #     return self.req.get(api_url,
    #                         headers=self.session.get_headers()).json()

    def save(self, obj):
        pass

    def update(self, obj):
        pass

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
        #
        # return requests.delete(url, data=json.dumps(data),
        #                        headers=self.header).json()

    def auth(self, user_id, checkout):
        """Привязка карты получателю."""
        url = self(self.base_path, 'auth')
        return self.req.post(url, json.dumps(
            dict(CardholderName='NONE', CardCryptogramPacket=checkout,
                 UserId=user_id)), headers=self.session.get_headers()).json()
