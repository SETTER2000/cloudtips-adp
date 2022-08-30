"""Top-level package for cloudtipsadp API Python Client Library."""

from .api import (  # noqa: F401
    token,
    headers,
    token_refresh,
    accums_summary,
    accums_payout_receiver,
    cards_3ds,
    cards_add,
    cards_auth,
    cards_default,
    cards_delete,
    cards_get,
    cards_get,
    receivers_create,
    payouts,
    places_confirm,
    places_get,
    places_send_sms,
    receivers_get,
    receivers_detach_agent,
    receivers_pages,
    receivers_photo,
)

__version__ = '0.15.0'
__author__ = "SETTER"
__email__ = 'lphp@mail.ru'
