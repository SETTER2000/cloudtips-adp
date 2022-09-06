from dependency_injector.wiring import Provide, inject

from src.cloudtipsadp.connect.repository import Repository
from src.cloudtipsadp.containers import Container


@inject
def payout(filters=None,
           repository: Repository = Provide[Container.payout_repository]):
    return repository().provider().list(filters=filters)
