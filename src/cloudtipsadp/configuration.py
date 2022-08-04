class Configuration(object):
    """
    A class representing the configuration.
    """
    api_url = "https://api.cloudtips.ru/api"
    account_id = None
    secret_key = None
    timeout = 1800
    max_attempts = 3
    auth_token = None

    @staticmethod
    def configure_auth_token(token, **kwargs):
        Configuration.account_id = None
        Configuration.secret_key = None
        Configuration.auth_token = token
        Configuration.timeout = kwargs.get("timeout", 1800)
        Configuration.max_attempts = kwargs.get("max_attempts", 3)


# if __name__ == '__main__':
#     Configuration.configure_auth_token('wegtehytr65', timeout=2000)
#     print(Configuration.__dict__)
