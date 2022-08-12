import pytest

from src.cloudtipsadp.clients import Connect, SandboxClient
from src.cloudtipsadp import Cloudtipsadp


connect = Connect(SandboxClient())
cta = Cloudtipsadp()


def res(response=None, text: str = None):
    if response:
        print(text)
        print(response.get('data'))
    else:
        print(response.get('errors'))


def get_token():
    token = connect.get_token()
    print(f'TOKEN:: {token}')


def refresh_token():
    token = connect.refresh_token()
    print(f'REFRESH TOKEN:: {token}')


def create_receiver():
    """Создать получателя."""
    response = cta.receiver_create(cta.receivers('Adam', '+79162047558'))
    res(response, 'Получатель создан:')


def get_places():
    """Информация по всем заведениям ТСП."""
    response = cta.place_get(cta.places())
    res(response, 'Все заведения:')


def get_cards(user_id):
    """Получение списка карт получателя."""
    response = cta.card_get(cta.cards(user_id))
    res(response, 'Список карт получателя:')


def get_sum(user_id):
    """Получить общую сумму донатов, по сотруднику."""
    response = cta.acc_get(cta.accum(user_id))
    res(response, 'Cумму донатов, по сотруднику:')
