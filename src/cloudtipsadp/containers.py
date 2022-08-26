"""
Здесь можно создать несколько классов, для каждой сущности проекта (как
вариант). Вместо того чтоб создавать один Container.
Например: UserContainer, DatabaseContainer
"""

from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide

from src.cloudtipsadp.connect.sessions import Session
from src.cloudtipsadp.connect.unit_of_work import CloudtipsUnitOfWork
from src.cloudtipsadp.payouts_pak.connect.repository import PayoutRepository
from src.cloudtipsadp.connect.repository import Repository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=['payouts_pak']
    )
    session_creator = providers.Factory(Session)
    # print(f'SESSION CREATOR:: {session_creator}')
    payout_repository = providers.Factory(PayoutRepository,
                                          session=session_creator)
    # print(f'PAYOUTS REPOSITORY:: {payouts_repository().list()}')
    payouts_uow = providers.Factory(CloudtipsUnitOfWork,
                                    repository=payout_repository)


@inject
def list_payouts(
        repository: Repository = Provide[Container.payout_repository]):
    return repository.list()


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    list_payouts()
