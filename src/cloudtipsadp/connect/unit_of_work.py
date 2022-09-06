from abc import ABC, abstractmethod

from cloudtipsadp.connect.repository import Repository


class UnitOfWork(ABC):
    """Слой управления сессий подключения. Менеджер транзакций."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.session = repository.session

    @abstractmethod
    def begin(self):
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        raise NotImplementedError()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()

    def __enter__(self):
        self.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()


class CloudtipsUnitOfWork(UnitOfWork):
    """Cloudtips service. Connect session."""
    def begin(self):
        self.session.get_token()

    def rollback(self):
        self.session.refresh_token()

    def commit(self):
        self.session.commit()
