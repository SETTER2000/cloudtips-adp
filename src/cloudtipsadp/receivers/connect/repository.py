import json
import os

import magic
import requests

from cloudtipsadp.connect.clients import Connect
from cloudtipsadp.connect.repository import Repository
from cloudtipsadp import constants as cnt

try:
    from simplejson import JSONDecodeError
except ImportError:
    from json import JSONDecodeError


class ReceiverRepository(Repository):
    """Получатель."""
    receivers = list()
    phone_number: str

    def __init__(self,
                 req: requests = None,
                 session: Connect = None,
                 base_path: str = None, ):
        super(ReceiverRepository, self).__init__(req, session, base_path)

    def get(self, obj_id: str):
        """Получателя по id выбрать."""
        try:
            url = self(self.base_path, obj_id)
            return self.req.get(url, headers=self.session.get_headers()).json()
        except JSONDecodeError:
            print(cnt.CTA, cnt.JSON_ERR_OBJECT)

    def list(self):
        """Все получатели в заведении."""
        try:
            api_url = self(self.base_path)
            return self.req.get(api_url,
                                headers=self.session.get_headers()).json()
        except JSONDecodeError:
            print(cnt.CTA, cnt.JSON_ERR_OBJECT)

    def save(self, obj):
        """Создать получателя донатов в сервисе."""
        try:
            url = self(self.base_path, 'create-many')
            return self.req.post(url, data=json.dumps(obj),
                                 headers=self.session.get_headers()).json()
        except JSONDecodeError:
            print(cnt.CTA, cnt.JSON_ERR_OBJECT)

    def update(self, obj):
        pass

    def detach_agent(self, user_id):
        """Удалить получателя из скоупа."""
        try:
            url = self(self.base_path, user_id, 'detach-agent')
            parsed = self.req.post(url,
                                   headers=self.session.get_headers()).json()
        except TypeError:
            print('NotFound user_id.')
        except JSONDecodeError:
            print(cnt.CTA, cnt.JSON_ERR_OBJECT)
        else:
            return parsed

    def photo_load(self, user_id, photo_path):
        """Загрузить фотографию получателя."""
        payload = {}
        try:
            paths = os.path.split(photo_path)
            with open(photo_path, 'rb') as file:
                files = [
                    ('FormFile', (paths[1], file,
                                  magic.from_file(photo_path, mime=True)))
                ]
                url = self(self.base_path, user_id, 'photo')
                parsed = requests.post(
                    url, headers=Connect.get_headers_token(), data=payload,
                    files=files).json()
        except FileNotFoundError as e:
            print(f'{cnt.FILE_PATH_BAD} {e}')
        except JSONDecodeError:
            print(cnt.CTA, cnt.JSON_ERR_OBJECT)
        else:
            return parsed
