from dependency_injector.wiring import Provide, inject

from cloudtipsadp.connect.repository import Repository
from cloudtipsadp.containers import Container
from cloudtipsadp.receivers.connect.models import Receiver


@inject
def receiver_get(
        user_id: str,
        repository: Repository = Provide[Container.receiver_repository]):
    return repository().provider().get(obj_id=user_id)


@inject
def receiver_detach_agent(
        user_id: str,
        repository: Repository = Provide[Container.receiver_repository]):
    return repository().provider().detach_agent(user_id=user_id)


@inject
def receiver_create(
        phone_number: str, name: str,
        repository: Repository = Provide[Container.receiver_repository]):
    return repository().provider().save(
        Receiver(phone=phone_number, name=name).data)


@inject
def photo_load(
        user_id: str, photo_path: str,
        repository: Repository = Provide[Container.receiver_repository]):
    return repository().provider().photo_load(
        user_id=user_id, photo_path=photo_path)


@inject
def receiver_pages(
        repository: Repository = Provide[Container.receiver_repository]):
    return repository().provider().list()
