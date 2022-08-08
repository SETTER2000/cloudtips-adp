from src.cloudtipsadp import Connect, SandboxClient
from src.cloudtipsadp.constants import M_BASE_IMPLEMENTED
import requests as requests


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
        if response.ok:
            return response.json()
        # elif response.status_code == 415:
        #     connect.refresh_token()
        #     self.create()
        return None


if __name__ == '__main__':
    connect = Connect(SandboxClient())
    ob = Places().get()
    if ob:
        print(f'Все заведения: {ob}')
