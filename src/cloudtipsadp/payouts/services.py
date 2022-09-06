from dependency_injector.wiring import Provide, inject

from cloudtipsadp.connect.repository import Repository
from cloudtipsadp.containers import Container


@inject
def payout(filters=None,
           repository: Repository = Provide[Container.payout_repository]):
    return repository().provider().list(filters=filters)
