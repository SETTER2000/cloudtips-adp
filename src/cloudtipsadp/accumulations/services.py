from dependency_injector.wiring import Provide, inject

from cloudtipsadp.connect.repository import Repository
from cloudtipsadp.containers import Container


@inject
def accum_summary(
        user_id: str,
        repository: Repository = Provide[Container.accumulation_repository]):
    return repository().provider().get(user_id)


@inject
def accum_payout_receiver(
        user_id: str,
        repository: Repository = Provide[Container.accumulation_repository]):
    return repository().provider().payout_receiver(user_id)
