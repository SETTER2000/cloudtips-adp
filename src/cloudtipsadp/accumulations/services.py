from dependency_injector.wiring import inject, Provide
from src.cloudtipsadp.containers import Container
from src.cloudtipsadp.connect.repository import Repository


@inject
def accum_summary(
        user_id: str,
        repository: Repository = Provide[Container.accumulation_repository]):
    return repository().provider().get(obj_id=user_id)


@inject
def accum_payout_receiver(
        user_id: str,
        repository: Repository = Provide[Container.accumulation_repository]):
    return repository().provider().payout_receiver(user_id=user_id)
