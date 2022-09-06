import requests

from cloudtipsadp.connect.clients import Connect
from cloudtipsadp.connect.repository import Repository
from cloudtipsadp import constants as cnt

try:
    from simplejson import JSONDecodeError
except ImportError:
    from json import JSONDecodeError


class AccumulationRepository(Repository):
    """Выплата."""

    def __init__(self,
                 req: requests = None,
                 session: Connect = None,
                 base_path: str = None, ):
        super(AccumulationRepository, self).__init__(req, session, base_path)

    def get(self, obj_id):
        """Накопления получателя."""
        try:
            url = self(self.base_path, obj_id, 'summary')
            return self.req.get(url, headers=self.session.get_headers()).json()
        except JSONDecodeError:
            print(cnt.CTA, cnt.JSON_ERR_OBJECT)

    def list(self):
        raise NotImplementedError()

    def save(self, obj):
        self.session.add(obj)

    def update(self, obj):
        raise NotImplementedError()

    def payout_receiver(self, user_id):
        """Выплата накопления получателю."""
        try:
            url = self(self.base_path, 'payout', user_id)
            return self.req.post(url,
                                 headers=self.session.get_headers()).json()
        except JSONDecodeError:
            print(cnt.CTA, cnt.JSON_ERR_OBJECT)
