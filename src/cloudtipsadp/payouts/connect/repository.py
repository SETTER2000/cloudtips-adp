from cloudtipsadp.connect.repository import Repository
from cloudtipsadp import constants as cnt

try:
    from simplejson import JSONDecodeError
except ImportError:
    from json import JSONDecodeError


class PayoutRepository(Repository):
    """Выплата."""

    def list(self, filters=None):
        """Получение всех транзакций выплат получателям менеджера."""
        try:
            url = self(self.base_path)
            return self.req.get(url, params=filters,
                                headers=self.session.get_headers()).json()
        except JSONDecodeError:
            print(cnt.CTA, cnt.JSON_ERR_OBJECT)

    def get(self, obj_id: str):
        raise NotImplementedError()

    def save(self, obj):
        self.session.add(obj)

    def update(self, obj):
        raise NotImplementedError()
