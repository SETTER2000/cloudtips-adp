"""
Здесь можно создать несколько классов, для каждой сущности проекта (как
вариант). Вместо того чтоб создавать один Container.
Например: UserContainer, DatabaseContainer
"""
import requests
from dependency_injector import containers, providers
from src.cloudtipsadp.connect.sessions import Session
from src.cloudtipsadp.connect.unit_of_work import CloudtipsUnitOfWork
from src.cloudtipsadp.payouts_pak.connect.repository import PayoutRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=['payouts_pak'])

    session_creator = providers.Factory(Session)
    payout_repository = providers.Factory(
        PayoutRepository, req=requests, session=session_creator,
        base_path='payout')
    payouts_uow = providers.Factory(
        CloudtipsUnitOfWork, repository=payout_repository)
