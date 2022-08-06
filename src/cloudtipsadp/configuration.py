class Token:
    access_token: str
    expires_in: int
    token_type: str
    refresh_token: str
    scope: str

    def refresh(self):
        return self.refresh_token


class Configuration(object):
    """
    A class representing the configuration.
    """
    _api_url = "https://api.cloudtips.ru/api"
    _api_url_sandbox = "https://api.cloudtips.ru/api"
    account_id = None
    secret_key = None
    timeout = 1800
    max_attempts = 3
    auth_token = None

    @staticmethod
    def configure_auth_token(access_token, **kwargs):
        Configuration.account_id = None
        Configuration.secret_key = None
        Configuration.auth_token = access_token
        Configuration.timeout = kwargs.get("timeout", 1800)
        Configuration.max_attempts = kwargs.get("max_attempts", 3)

# if __name__ == '__main__':
#     Configuration.configure_auth_token('wegtehytr65', timeout=2000)
#     print(Configuration.__dict__)
