import requests as requests

from src.cloudtipsadp import Connect, SandboxClient
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED


class Place:
    """Заведения."""
    base_path = 'places'

    def get(self):
        raise NotImplementedError(M_BASE_IMPLEMENTED)


class Places(Place):
    def get(self):
        """Позволяет получить информацию по всем заведениям ТСП."""
        # URL для запроса к API
        api_url = Connect.client.api([self.base_path])
        response = requests.get(api_url, headers=Connect.get_headers())
        return response.json()


if __name__ == '__main__':
    connect = Connect(SandboxClient())
    places = Places().get()
    if places:
        print(f'Все заведения: {places.get("data")}')
