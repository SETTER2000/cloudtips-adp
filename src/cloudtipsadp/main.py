from typing import Type

from src.cloudtipsadp.accumulations.services import (
    accum_summary, accum_payout_receiver)
from src.cloudtipsadp.cards.services import (card_delete, card_default,
                                             card_get, card_auth)
from src.cloudtipsadp.payouts.services import (payout, )
# from src.cloudtipsadp.accumulations import Accumulation, Accumulations
# from src.cloudtipsadp.cards import Card, Cards, FlowBase
from src.cloudtipsadp.clients import Connect, ProductClient, SandboxClient
# from src.cloudtipsadp.places import Place, Places
from src.cloudtipsadp.places.services import (place_send, place_confirm,
                                              place_list)
# from src.cloudtipsadp.receivers.services import
from src.cloudtipsadp.receivers.services import (
    receiver_detach_agent, receiver_pages, photo_load, receiver_get,
    receiver_create)


class Cloudtipsadp:
    __link = None

    def __init__(self):
        # class
        self.__connect = Connect
        self.__sandbox_client = SandboxClient
        self.__product_client = ProductClient
        # self.accums: Type[Accumulation] = Accumulations
        self.accums_summary = accum_summary
        self.accums_payout_receiver = accum_payout_receiver
        self.cards_auth = card_auth
        self.cards_delete = card_delete
        self.cards_default = card_default
        self.cards_get = card_get
        # self.cards_flow = _card_flow
        self.payouts = payout
        self.places_confirm = place_confirm
        self.places_get = place_list
        self.places_send_sms = place_send
        self.receivers_create = receiver_create
        self.receivers_get = receiver_get
        self.receivers_detach_agent = receiver_detach_agent
        self.receivers_pages = receiver_pages
        self.receivers_photo = photo_load

    def connect(self, sandbox=False):
        """Подключение."""
        if sandbox:
            self.__link = self.__connect(self.__sandbox_client())
        self.__link = self.__connect()

    def get_token(self):
        return self.__connect.get_token()

    def refresh_token(self):
        return self.__link.refresh_token()


#
# def _accum_summary(accumulation: Accumulation):
#     """Накопления по получателю."""
#     return accumulation.summary()
#
#
# def _accum_payout_receiver(accumulation: Accumulation):
#     """Выплата накопления получателю."""
#     return accumulation.payout_receiver()


#
# def _card_auth(card: Card):
#     """Отправить криптограмму."""
#     return card.auth()
#
#
# def _card_default(card: Card):
#     """Изменить карту, на которую выплачиваются чаевые по умолчанию."""
#     return card.default()
#
#
# def _card_delete(card: Card):
#     """Удаление карты получателя. Карту по умолчанию удалить нельзя."""
#     return card.delete()
#
#
# def _card_get(card: Card):
#     """Список карт получателя."""
#     return card.get()
#
#
# def _card_flow(flow: FlowBase):
#     if isinstance(flow, FlowBase):
#         return flow.auth()
#     else:
#         print('Error, type mismatch.')
#

# def _payout_get(payout: Payout):
#     """ Получение всех транзакций выплат получателям менеджера."""
#     return payout.get()
#

# def _payout_list():
#     """ Получение всех транзакций выплат получателям менеджера."""
#     return list_payouts()

#
# def _place_confirm(place: Place):
#     """
#     Передать код из смс.
#     Подтверждение привязки телефона (пользователя) к предприятию.
#     """
#     return place.confirm()
#
#
# def _place_get(place: Place):
#     """Информация по всем заведениям ТСП."""
#     return place.get()
#
#
# def _place_send(place: Place):
#     """
#     Привязка получателя к заведению.
#     Отправить сотруднику на его номер телефона код в смс сообщении.
#     """
#     return place.send()
#

# def _receiver_create(receiver: Receiver):
#     """Создать получателя донатов."""
#     return receiver.create()

#
# def _receiver_detach_agent(receiver: Receiver):
#     """Удалить получателя из скоупа."""
#     return receiver.detach_agent()
#
#
# def _receiver_pages(receiver: Receiver):
#     """Все получатели донатов."""
#     return receiver.pages()
#
#
# def _receiver_photo(receiver: Receiver):
#     """Загрузить фотографию получателя."""
#     return receiver.photo()
#

if __name__ == '__main__':
    from src.cloudtipsadp import Cloudtipsadp

    cta = Cloudtipsadp()
    user_id = '44a38440-595d-494e-a028-09804355757a'
    photo_path = '/home/setter/Изображения/Adam.jpg'

    # response = cta.receivers_get(
    #     user_id='44a38440-595d-494e-a028-09804355757a')
    # print(response)
    # response = cta.payouts()
    # print(response)
    # response = cta.receivers_create(name='Adam', phone_number='+79162047558')
    # print(response)
    # response = cta.receivers_pages()
    # print(response)
    # response = cta.receivers_detach_agent(
    #     '44a38440-595d-494e-a028-09804355757a')
    # print(response)
    # response = cta.places_send_sms('44a38440-595d-494e-a028-09804355757a')
    # print(response)
    #

    # response = cta.receivers_photo(user_id=user_id, photo_path=photo_path)
    # if type(response) == dict and response.get('succeed'):
    #     print('Фото получателя успешно загружено:')
    #     print(response.get('data'))
    # else:
    #     print(f'RESPONSE: {response}')
    #
    # response = cta.places_confirm(user_id=user_id, code='000000')
    # if type(response) == dict and response.get('succeed'):
    #     print('Подтвердить привязку телефона. Передать код из смс:')
    #     print(response.get('data'))
    # else:
    #     print(f'RESPONSE: {response}')

    # response = cta.places_get()
    # if type(response) == dict and response.get('succeed'):
    #     print('Позволяет получить информацию по всем заведениям ТСП:')
    #     print(response.get('data'))
    # else:
    #     print(f'RESPONSE: {response}')

    # response = cta.cards_get(user_id)
    # if type(response) == dict and response.get('succeed'):
    #     print('Список карт получателя:')
    #     print(response.get('data'))
    # else:
    #     print(f'RESPONSE: {response}')

    # response = cta.cards_default(user_id, card_token='124234234234234')
    # if type(response) == dict and response.get('succeed'):
    #     print('Изменить карту, на которую выплачиваются чаевые по умолчанию:')
    #     print(response.get('data'))
    # else:
    #     print(f'RESPONSE: {response}')

    # response = cta.cards_delete(user_id, card_token='124234234234234')
    # if type(response) == dict and response.get('succeed'):
    #     print('Изменить карту, на которую выплачиваются чаевые по умолчанию:')
    #     print(response.get('data'))
    # else:
    #     print(f'RESPONSE66: {response}')
    #
    # response = cta.cards_auth(user_id, checkout='124234234234234')
    # if type(response) == dict and response.get('succeed'):
    #     print('Привязка карты получателю:')
    #     print(response.get('data'))
    # else:
    #     print(f'RESPONSE-87: {response}')
    #
    # response = cta.accums_summary(user_id)
    # if type(response) == dict and response.get('succeed'):
    #     print('Накопления получателя:')
    #     print(response.get('data'))
    # else:
    #     print(f'RESPONSE-87: {response}')

    response = cta.accums_payout_receiver(user_id)
    if type(response) == dict and response.get('succeed'):
        print('Выплата накопления получателю:')
        print(response.get('data'))
    else:
        print(f'RESPONSE-0: {response}')
