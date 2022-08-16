from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    access_token: str
    expires_in: int
    token_type: str
    refresh_token: str
    scope: str

    def refresh(self):
        return self.refresh_token


# @dataclass(frozen=True)
class Filter:
    dateFrom: str
    dateTo: str
    phoneNumber: str
    layoutId: str
    id: str
    status: str
    userId: str
    page: str
    limit: str
