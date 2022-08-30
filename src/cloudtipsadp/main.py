from src.cloudtipsadp import settings
from src.cloudtipsadp.accumulations.services import (
    accum_payout_receiver, accum_summary)
from src.cloudtipsadp.cards.services import (
    card_auth, card_default, card_delete, card_get, card_add, card_3ds,
    token_connect, token_refresh, headers_get)
from src.cloudtipsadp.payouts.services import payout
from src.cloudtipsadp.places.services import (
    place_confirm, place_list, place_send)
from src.cloudtipsadp.receivers.services import (
    photo_load, receiver_create, receiver_detach_agent, receiver_get,
    receiver_pages)


class Cloudtipsadp:
    __link = None

    def __init__(self):
        self.accums_summary = accum_summary
        self.accums_payout_receiver = accum_payout_receiver
        self.cards_3ds = card_3ds
        self.cards_add = card_add
        self.cards_auth = card_auth
        self.cards_delete = card_delete
        self.cards_default = card_default
        self.cards_get = card_get
        self.get_token = token_connect
        self.refresh_token = token_refresh
        self.get_headers = headers_get
        self.payouts = payout
        self.places_confirm = place_confirm
        self.places_get = place_list
        self.places_send_sms = place_send
        self.receivers_create = receiver_create
        self.receivers_get = receiver_get
        self.receivers_detach_agent = receiver_detach_agent
        self.receivers_pages = receiver_pages
        self.receivers_photo = photo_load


if __name__ == '__main__':
    cta = Cloudtipsadp()
    user_id = '44a38440-595d-494e-a028-09804355757a'
    photo_path = '/home/setter/Изображения/Adam.jpg'
    checkout = '014242424242250102CmRUh+v/FysG8c2kGbrJttFXCqHUJDohTXLJb8Wqpq9'
    print(f'settings.BASE_URL:::: {settings.BASE_URL}')
    print(f'TOKEN: {cta.get_token()}')
    # print(f'HEADERS+TOKEN: {cta.get_headers()}')
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
    # transact_id = 'AQ=='
    # TODO здесь надо в метод /api/cards/post3ds отправлять, а потом в add
    # response = cta.cards_add(user_id, transact_id)
    # if type(response) == dict and response.get('succeed'):
    #     print('Подтвердить привязку карты на стороне системы:')
    #     print(response.get('data'))
    # else:
    #     print(f'ERR-007: {response}')
