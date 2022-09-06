from abc import ABC, abstractmethod

import requests

from cloudtipsadp.connect.clients import Connect


class Repository(ABC):
    def __init__(self, req: requests, session: Connect, base_path: str):
        self.req = req
        self.session = session
        self.base_path = base_path

    @abstractmethod
    def get(self, obj_id: str):
        raise NotImplementedError()

    @abstractmethod
    def list(self):
        raise NotImplementedError()

    @abstractmethod
    def save(self, obj):
        raise NotImplementedError()

    @abstractmethod
    def update(self, obj):
        raise NotImplementedError()

    def __call__(self, *args, **kwargs):
        return self.session.client.api(list(args))
