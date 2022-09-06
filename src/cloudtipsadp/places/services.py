from dependency_injector.wiring import Provide, inject

from cloudtipsadp.connect.repository import Repository
from cloudtipsadp.containers import Container


@inject
def place_list(
        repository: Repository = Provide[Container.place_repository]):
    return repository().provider().list()


@inject
def place_send(
        user_id: str,
        repository: Repository = Provide[Container.place_repository]):
    return repository().provider().send(user_id=user_id)


@inject
def place_confirm(
        user_id: str, code: str,
        repository: Repository = Provide[Container.place_repository]):
    return repository().provider().confirm(user_id=user_id, code=code)
