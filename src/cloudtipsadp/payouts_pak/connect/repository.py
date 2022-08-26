from src.cloudtipsadp.connect.repository import Repository


class PayoutRepository(Repository):
    """Выплаты."""
    def get(self):
        """Получение всех транзакций выплат получателям менеджера."""
        url = self(self.base_path)
        return self.req.get(url, headers=self.header).json()

    def list(self):
        print('Hello, SETTER!!!')

    def save(self, obj):
        self.session.add(obj)

    def update(self, obj):
        raise NotImplementedError()

#
# if __name__ == '__main__':
#     from src.cloudtipsadp.connect.sessions import Session
#     p = PayoutRepository(session=Session)
#     p.list()
