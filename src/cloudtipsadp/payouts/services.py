from dependency_injector.wiring import inject, Provide
from src.cloudtipsadp.containers import Container
from src.cloudtipsadp.connect.repository import Repository
from src.cloudtipsadp.connect.unit_of_work import UnitOfWork


@inject
def payout(
        repository: Repository = Provide[Container.payout_repository]):
    return repository().provider().list()
