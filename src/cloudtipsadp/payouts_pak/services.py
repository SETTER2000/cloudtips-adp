from dependency_injector.wiring import inject, Provide
from src.cloudtipsadp.containers import Container
from src.cloudtipsadp.connect.repository import Repository
from src.cloudtipsadp.connect.unit_of_work import UnitOfWork


@inject
def list_payouts(
        repository: Repository = Provide[Container.payout_repository]):
    return repository().provider().list()


# @inject
# def list_payouts(unit_of_work: UnitOfWork = Provide[Container.payouts_uow]):
#     with unit_of_work:
#         return unit_of_work.repository.list()

if __name__ == "__main__":
    from src.cloudtipsadp.containers import Container
    container = Container()
    container.wire(modules=[__name__])

    list_payouts()
