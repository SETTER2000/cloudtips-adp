import json

from cloudtipsadp.constants import M_BASE_IMPLEMENTED, SITE_RETURNING_URL


class FlowBase:
    """Варианты авторизации карт."""

    def __init__(self, transactionId: int):
        self.transactionId = transactionId

    def auth(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Frictionless(FlowBase):
    """Карта не 3ds, либо получатель уже проходил авторизацию ранее."""

    def auth(self):
        pass


class Challenge(FlowBase):
    """Карта c 3ds и нужно подтверждение с вводом кода из sms."""

    def __init__(
            self,
            transactionId,
            md: str,
            paReq: str,
            acsUrl: str,
            statusCode: str,
            message: str = None,
            cardToken: str = None,
            issuerCode: str = None,
            otpRequired: str = None,
            cardIssuerBankCountry: str = None,
            cardLastFour: str = None,
            cardExpDate: str = None):
        super(Challenge, self).__init__(transactionId)
        self.md = md
        self.paReq = paReq
        self.acsUrl = acsUrl
        self.message = message
        self.statusCode = statusCode
        self.cardToken = cardToken
        self.issuerCode = issuerCode
        self.otpRequired = otpRequired
        self.cardIssuerBankCountry = cardIssuerBankCountry
        self.cardLastFour = cardLastFour
        self.cardExpDate = cardExpDate

    def __get_data(self):
        try:
            data = dict(MD=self.md,
                        PaReq=self.paReq,
                        TermUrl=SITE_RETURNING_URL)
        except AttributeError:
            print('No user data.')
        else:
            return json.dumps(data)
