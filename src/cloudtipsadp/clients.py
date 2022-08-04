import requests as requests


class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_get_request(self):
        res = requests.get(self.base_url)
        return res.json()

    def __call__(self, *args, **kwargs):
        return self.make_get_request()


class SandboxClient(BaseClient):
    pass


class WikiClient(BaseClient):
    pass


class Worker:
    def __init__(self, sandbox_client: SandboxClient, wiki_client: WikiClient):
        self.sandbox_client = sandbox_client
        self.wiki_client = wiki_client

    def __call__(self, *args, **kwargs):
        return {'wiki_data': self.wiki_client(),
                'sandbox_client': self.sandbox_client}


