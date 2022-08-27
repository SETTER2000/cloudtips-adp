from dependency_injector.wiring import Provide, inject

from src.cloudtipsadp.connect.repository import Repository
from src.cloudtipsadp.containers import Container


@inject
def place_list(
        repository: Repository = Provide[Container.place_repository]):
    return repository().provider().list()


@inject
def card_get(
        user_id: str,
        repository: Repository = Provide[Container.card_repository]):
    return repository().provider().get(obj_id=user_id)


@inject
def place_confirm(
        user_id: str, code: str,
        repository: Repository = Provide[Container.place_repository]):
    return repository().provider().confirm(user_id=user_id, code=code)


@inject
def card_default(user_id: str, card_token: str,
                 repository: Repository = Provide[Container.card_repository]):
    return repository().provider().default(
        user_id=user_id, card_token=card_token)


@inject
def card_delete(user_id: str, card_token: str,
                repository: Repository = Provide[Container.card_repository]):
    return repository().provider().delete(user_id=user_id,
                                          card_token=card_token)


@inject
def card_auth(user_id: str, checkout: str,
              repository: Repository = Provide[Container.card_repository]):
    return repository().provider().auth(user_id=user_id,
                                        checkout=checkout)
