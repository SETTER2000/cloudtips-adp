"""
Здесь можно создать несколько классов, для каждой сущности проекта (как
вариант). Вместо того чтоб создавать один Container.
Например: UserContainer, DatabaseContainer
"""
import requests
from dependency_injector import containers, providers

from src.cloudtipsadp.accumulations.connect.repository import \
    AccumulationRepository
from src.cloudtipsadp.cards.connect.repository import CardRepository
from src.cloudtipsadp.connect.sessions import Session
from src.cloudtipsadp.connect.unit_of_work import CloudtipsUnitOfWork
from src.cloudtipsadp.payouts.connect.repository import PayoutRepository
from src.cloudtipsadp.places.connect.repository import PlaceRepository
from src.cloudtipsadp.receivers.connect.repository import ReceiverRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=['payouts', 'receivers', 'places', 'cards', 'accumulation'])
    session_creator = providers.Factory(Session)

    # Payouts
    payout_repository = providers.Factory(
        PayoutRepository, req=requests, session=session_creator,
        base_path='payout')

    # Receivers
    receiver_repository = providers.Factory(
        ReceiverRepository, req=requests, session=session_creator,
        base_path='receivers')

    # Places
    place_repository = providers.Factory(
        PlaceRepository, req=requests, session=session_creator,
        base_path='places')

    # Cards
    card_repository = providers.Factory(
        CardRepository, req=requests, session=session_creator,
        base_path='cards')

    # Cards
    accumulation_repository = providers.Factory(
        AccumulationRepository, req=requests, session=session_creator,
        base_path='accumulations')
