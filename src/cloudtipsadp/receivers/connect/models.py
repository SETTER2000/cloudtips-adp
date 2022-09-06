from cloudtipsadp import settings


class Receiver:
    def __init__(self, phone: str, name: str, ):
        self.phone_number = phone
        self.name = name

    @property
    def data(self):
        try:
            receivers = [dict(phoneNumber=self.phone_number, name=self.name)]
            data = dict(placeId=settings.CTA_PLACE_ID, receivers=receivers)
        except AttributeError:
            print('No user data.')
            return None
        else:
            return data
