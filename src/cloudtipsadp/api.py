from cloudtipsadp.accumulations.services import (
    accum_payout_receiver, accum_summary)
from cloudtipsadp.cards.services import (
    card_auth, card_default, card_delete, card_get, card_add, card_3ds,
    token_connect, token_ref, headers_get)
from cloudtipsadp.payouts.services import payout
from cloudtipsadp.places.services import (
    place_confirm, place_list, place_send)
from cloudtipsadp.receivers.services import (
    photo_load, receiver_create, receiver_detach_agent, receiver_get,
    receiver_pages)


def token():
    """Return Header & Token."""
    return token_connect()


def token_refresh() -> str:
    """Return Refresh Token."""
    return token_ref()


def headers() -> dict:
    """Return Header & Token."""
    return headers_get()


def accums_summary(user_id: str):
    """Накопления получателя."""
    return accum_summary(user_id)


def accums_payout_receiver(user_id: str):
    """Выплата накопления получателю."""
    return accum_payout_receiver(user_id)


def cards_3ds(user_id: str, md: str, paRes: str):
    """Для проведения 3-D Secure аутентификации."""
    return card_3ds(user_id=user_id, md=md, paRes=paRes)


def cards_add(user_id: str, transact_id: str):
    """
    При успешном окончании методов 3, 4 или 5 необходимо подтвердить
    привязку карты на стороне системы.
    """
    return card_add(user_id=user_id, transact_id=transact_id)


def cards_auth(user_id: str, checkout: str):
    """Привязка карты получателю."""
    return card_auth(user_id=user_id, checkout=checkout)


def cards_default(user_id: str, card_token: str):
    """Изменить карту, на которую выплачиваются чаевые по умолчанию."""
    return card_default(user_id=user_id, card_token=card_token)


def cards_delete(user_id: str, card_token: str):
    """Удаление карты получателя. Карту по умолчанию удалить нельзя."""
    return card_delete(user_id=user_id, card_token=card_token)


def cards_get(user_id: str):
    """Список карт получателя."""
    return card_get(user_id=user_id)


def payouts(filters: dict = None):
    """Получение всех транзакций выплат получателям менеджера."""
    return payout(filters)


def places_confirm(user_id: str, code: str):
    """
    Подтвердить привязку телефона (пользователя) к предприятию.
    Передать код из смс.
    """
    return place_confirm(user_id=user_id, code=code)


def places_get():
    """Позволяет получить информацию по всем заведениям ТСП."""
    return place_list()


def places_send_sms(user_id: str):
    """
    Привязка получателя к заведению.
    Отправить сотруднику на его номер телефона код в смс сообщении.
    """
    return place_send(user_id=user_id)


def receivers_create(phone_number: str, name: str):
    """Создать получателя донатов в сервисе."""
    return receiver_create(phone_number, name)


def receivers_detach_agent(user_id: str):
    """Удалить получателя из скоупа."""
    return receiver_detach_agent(user_id)


def receivers_get(user_id: str):
    """Получателя по id выбрать."""
    return receiver_get(obj_id=user_id)


def receivers_pages():
    """Все получатели в заведении."""
    return receiver_pages()


def receivers_photo(user_id: str, photo_path: str):
    """Загрузить фотографию получателя."""
    return photo_load(user_id=user_id, photo_path=photo_path)


if __name__ == '__main__':
    # user_id = '44a38440-595d-494e-a028-09804355757a'  # sandbox user
    user_id = '70e6531e-2d05-4f17-8f75-1bbe68d04c26'  # prod user

    photo_path = '/home/setter/Изображения/Adam.jpg'
    checkout = '014242424242250102CmRUh+v/FysG8c2kGbrJttFXCqHUJDohTXLJb8Wqpq9'
    # print(f'CARDS::: {cards_get(user_id=user_id)}')
    # print(f'CARDS_TYPE_3Ds::: '
    #       f'{}')
    # print(f'HEADERS+TOKEN: {headers()}')
    filters = dict(dateFrom='2022-08-01',
                   dateTo='2022-08-31',
                   phoneNumber='+78009005050',
                   userId=user_id,
                   limit=10)
    # filters = dict(userId=user_id)
    # filters = ''

    # res = payouts(filters)
    res = token()
    print(res)
    res = accums_summary(user_id)
    print(res)
    response = payouts(filters)
    # print(response)
    # print(result(response))
    # receivers_create(phone_number='+79162047558', name="Adam")
    # res = accums_summary(user_id=user_id)
    # print(res)

    # print(f'TOKEN REFRESH: {cta.refresh_token()}')
    ###############################################################
    # def res(response=None, text: str = None):
    #     if type(response) == dict and response.get('succeed'):
    #         print(text, response.get('data'))
    #         return response.get('data')
    #     else:
    #         print(response)
    #
    #
    # """Привязка карты получателю."""
    # response = cta.cards_auth(user_id=user_id, checkout=checkout)
    # resp = res(response, 'Отправить криптограмму:')
    # acsUrl = resp.get('acsUrl')
    # print(acsUrl)
    # acsUrl = 'https://acs.cloudpayments.ru/test-get'
    # md = resp.get('transactionId')
    # paReq = resp.get('paReq')
    # TermUrl = 'https://lphp.ru'
    # link = f'{acsUrl}/?PaReq={paReq}&MD={md}&TermUrl={TermUrl}'
    # print(link)

    # webbrowser.open_new_tab(link)
    #######################################
    #
    # ob = dict(PaReq=paReq, MD=md, TermUrl=TermUrl)
    # print(ob)
    # res = requests.get(link, params=ob).json()

    # print(f'RESPONSE=666::: {res}')

    # response = cta.cards_3ds(user_id=user_id, md=md, paRes=paReq)
    # if type(response) == dict and response.get('succeed'):
    #     print('Для проведения 3-D Secure аутентификации:')
    #     print(response.get('data'))
    # else:
    #     print(f'ERR-020: {response}')
    # print(f'GET TOKEn: {cta.get_token()}')
    # Step 1
    # data = cta.auth_cards(user_id, checkout)
    # print(f'RESP::: {data}')
    # # Step 2 transactionId
    ########################################################################
    #
    # TODO здесь надо в метод /api/cards/post3ds отправлять, а потом в add
    # cards_3ds(user_id=user_id, md=md, paRes=pa_res)
    # transact_id = 'AQ=='
    # response = cta.cards_add(user_id, transact_id)
    # if type(response) == dict and response.get('succeed'):
    #     print('Подтвердить привязку карты на стороне системы:')
    #     print(response.get('data'))
    # else:
    #     print(f'ERR-007: {response}')
