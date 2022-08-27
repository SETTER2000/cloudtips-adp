from dependency_injector.wiring import inject, Provide
from src.cloudtipsadp.containers import Container
from src.cloudtipsadp.connect.repository import Repository


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
