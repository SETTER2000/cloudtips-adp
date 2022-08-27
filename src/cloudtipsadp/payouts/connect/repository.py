from src.cloudtipsadp.connect.repository import Repository


class PayoutRepository(Repository):
    """Выплата."""

    def list(self):
        """Получение всех транзакций выплат получателям менеджера."""
        url = self(self.base_path)
        return self.req.get(url, headers=self.session.get_headers()).json()

    def get(self, obj_id: str):
        raise NotImplementedError()

    def save(self, obj):
        self.session.add(obj)

    def update(self, obj):
        raise NotImplementedError()
