from typing import Type

from src.cloudtipsadp.clients import (Connect, ProductClient, SandboxClient)
from src.cloudtipsadp.accumulations import Accumulation, Accumulations
from src.cloudtipsadp.cards import (Card, Cards, FlowBase)
from src.cloudtipsadp.places import Place, Places
from src.cloudtipsadp.receivers import Receivers, Receiver
from src.cloudtipsadp.payouts import Payouts, Payout


class Cloudtipsadp:
    __link = None

    def __init__(self):
        # class
        self.__connect = Connect
        self.__sandbox_client = SandboxClient
        self.__product_client = ProductClient
        self.accums: Type[Accumulation] = Accumulations
        self.cards = Cards
        self.payouts = Payouts
        self.places = Places
        self.receivers = Receivers
        # funcs
        self.accums_get = _accum_get
        self.cards_auth = _card_auth
        self.cards_get = _card_get
        self.cards_flow = _card_flow
        self.payouts_get = _payout_get
        self.places_confirm = _place_confirm
        self.places_get = _place_get
        self.places_send_sms = _place_send
        self.receivers_create = _receiver_create
        self.receivers_detach_agent = _receiver_detach_agent
        self.receivers_pages = _receiver_pages
        self.receivers_photo = _receiver_photo

    def connect(self, sandbox=False):
        """Подключение."""
        if sandbox:
            self.__link = self.__connect(self.__sandbox_client())
        self.__link = self.__connect()

    def get_token(self):
        return self.__connect.get_token()

    def refresh_token(self):
        return self.__link.refresh_token()


def _accum_get(accumulation: Accumulation):
    """Получить общую сумму донатов, по сотруднику."""
    return accumulation.get()


def _card_auth(card: Card):
    """Отправить криптограмму."""
    return card.auth()


def _card_get(card: Card):
    """Список карт получателя."""
    return card.get()


def _card_flow(flow: FlowBase):
    if isinstance(flow, FlowBase):
        return flow.auth()
    else:
        print('Error, type mismatch.')


def _payout_get(payout: Payout):
    """ Получение всех транзакций выплат получателям менеджера."""
    return payout.get()


def _place_confirm(place: Place):
    """
    Передать код из смс.
    Подтверждение привязки телефона (пользователя) к предприятию.
    """
    return place.confirm()


def _place_get(place: Place):
    """Информация по всем заведениям ТСП."""
    return place.get()


def _place_send(place: Place):
    """
    Привязка получателя к заведению.
    Отправить сотруднику на его номер телефона код в смс сообщении.
    """
    return place.send()


def _receiver_create(receiver: Receiver):
    """Создать получателя донатов."""
    return receiver.create()


def _receiver_detach_agent(receiver: Receiver):
    """Удалить получателя из скоупа."""
    return receiver.detach_agent()


def _receiver_pages(receiver: Receiver):
    """Все получатели донатов."""
    return receiver.pages()


def _receiver_photo(receiver: Receiver):
    """Загрузить фотографию получателя."""
    return receiver.photo()
