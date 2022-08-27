from src.cloudtipsadp.accumulations.services import (accum_payout_receiver,
                                                     accum_summary)
from src.cloudtipsadp.cards.services import (card_auth, card_default,
                                             card_delete, card_get)
from src.cloudtipsadp.payouts.services import payout
from src.cloudtipsadp.places.services import (place_confirm, place_list,
                                              place_send)
from src.cloudtipsadp.receivers.services import (photo_load, receiver_create,
                                                 receiver_detach_agent,
                                                 receiver_get, receiver_pages)


class Cloudtipsadp:
    __link = None

    def __init__(self):
        self.accums_summary = accum_summary
        self.accums_payout_receiver = accum_payout_receiver
        self.cards_auth = card_auth
        self.cards_delete = card_delete
        self.cards_default = card_default
        self.cards_get = card_get
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


if __name__ == '__main__':
    cta = Cloudtipsadp()
    user_id = '44a38440-595d-494e-a028-09804355757a'
    photo_path = '/home/setter/Изображения/Adam.jpg'

    response = cta.accums_payout_receiver(user_id)
    if type(response) == dict and response.get('succeed'):
        print('Выплата накопления получателю:')
        print(response.get('data'))
    else:
        print(f'RESPONSE-0: {response}')
