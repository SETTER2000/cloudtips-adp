from typing import Type

from loguru import logger

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
        self.receivers_pages = _receiver_pages
        self.receivers_photo = _receiver_photo

    @logger.catch
    def connect(self, sandbox=False):
        """Подключение."""
        if sandbox:
            self.__link = self.__connect(self.__sandbox_client())
        self.__link = self.__connect()

    @logger.catch
    def get_token(self):
        return self.__connect.get_token()

    @logger.catch
    def refresh_token(self):
        return self.__link.refresh_token()


@logger.catch
def _accum_get(accumulation: Accumulation):
    """Получить общую сумму донатов, по сотруднику."""
    return accumulation.get()


@logger.catch
def _card_auth(card: Card):
    """Отправить криптограмму."""
    return card.auth()


@logger.catch
def _card_get(card: Card):
    """Список карт получателя."""
    return card.get()


@logger.catch
def _card_flow(flow: FlowBase):
    if isinstance(flow, FlowBase):
        return flow.auth()
    else:
        print('Error, type mismatch.')


@logger.catch
def _payout_get(payout: Payout):
    """ Получение всех транзакций выплат получателям менеджера."""
    return payout.get()


@logger.catch
def _place_confirm(place: Place):
    """
    Передать код из смс.
    Подтверждение привязки телефона (пользователя) к предприятию.
    """
    return place.confirm()


@logger.catch
def _place_get(place: Place):
    """Информация по всем заведениям ТСП."""
    return place.get()


@logger.catch
def _place_send(place: Place):
    """
    Привязка получателя к заведению.
    Отправить сотруднику на его номер телефона код в смс сообщении.
    """
    return place.send()


@logger.catch
def _receiver_create(receiver: Receiver):
    """Создать получателя донатов."""
    return receiver.create()


@logger.catch
def _receiver_pages(receiver: Receiver):
    """Все получатели донатов."""
    return receiver.pages()


@logger.catch
def _receiver_photo(receiver: Receiver):
    """Загрузить фотографию получателя."""
    return receiver.photo()
