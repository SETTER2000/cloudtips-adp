from src.cloudtipsadp.clients import (Connect, ProductClient, SandboxClient)
from src.cloudtipsadp.accumulations import Accumulation, Accumulations
from src.cloudtipsadp.cards import (Card, Cards, FlowBase, Frictionless,
                                    Challenge)
from src.cloudtipsadp.places import Place, Places
from src.cloudtipsadp.receivers import Receivers, Receiver


class Cloudtipsadp:
    Connect = Connect
    ProductClient = ProductClient
    SandboxClient = SandboxClient
    cards = Cards
    accum = Accumulations
    places = Places
    receivers = Receivers

    def __init__(self):
        self.accums_get = _accum_get
        self.cards_auth = _card_auth
        self.cards_get = _card_get
        self.cards_flow = _card_flow
        self.places_confirm = _place_confirm
        self.places_get = _place_get
        self.places_send = _place_send
        self.receivers_create = _receiver_create


def _accum_get(accumulation: Accumulation):
    return accumulation.get()


def _card_auth(card: Card):
    return card.auth()


def _card_get(card: Card):
    return card.get()


def _card_flow(flow: FlowBase):
    if isinstance(flow, FlowBase):
        return flow.auth()
    else:
        print('Error, type mismatch.')


def _place_confirm(place: Place):
    return place.confirm()


def _place_get(place: Place):
    return place.get()


def _place_send(place: Place):
    return place.send()


def _receiver_create(receiver: Receiver):
    return receiver.create()
