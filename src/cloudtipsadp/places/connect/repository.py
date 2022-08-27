import json
import os

import magic
import requests

from src.cloudtipsadp.connect.clients import Connect
from src.cloudtipsadp.connect.repository import Repository
from src.cloudtipsadp.constants import FILE_PATH_BAD
from src.cloudtipsadp.settings import CTA_PLACE_ID


class PlaceRepository(Repository):
    """Заведения."""

    def __init__(self,
                 req: requests = None,
                 session: Connect = None,
                 base_path: str = None, ):
        super(PlaceRepository, self).__init__(req, session, base_path)

    def get(self, obj_id: str):
        pass

    def list(self):
        """Позволяет получить информацию по всем заведениям ТСП."""
        api_url = self(self.base_path)
        return self.req.get(api_url,
                            headers=self.session.get_headers()).json()

    def save(self, obj):
        pass

    def update(self, obj):
        pass

    def send(self, user_id):
        """
        Привязка получателя к заведению.
        Отправить сотруднику на его номер телефона код в смс сообщении.
        """
        url = self(self.base_path, CTA_PLACE_ID,
                   'employees', 'attach', 'send-sms')
        return self.req.post(url, data=json.dumps(dict(UserId=user_id)),
                             headers=self.session.get_headers()).json()

    def confirm(self, user_id, code):
        """
        Подтвердить привязку телефона (пользователя) к предприятию.
        Передать код из смс.
        """
        url = self(
            self.base_path, CTA_PLACE_ID, 'employees', 'attach', 'confirm')
        return self.req.post(
            url, data=json.dumps(dict(UserId=user_id, SmsCode=code)),
            headers=self.session.get_headers()).json()

    def delete(self, user_id, card_token):
        """Удаление карты получателя. Карту по умолчанию удалить нельзя."""
        url = self(self.base_path)
        return self.req.delete(url, dict(userId=user_id, cardToken=card_token))