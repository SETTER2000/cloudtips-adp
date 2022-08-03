from unittest import TestCase
from unittest.mock import patch, Mock

try:
    from src.cloudtipsadp.adp import CLoudTipsAdp as cta
except ModuleNotFoundError:
    assert False, 'Не найдена домашняя работа! :)'


class ServicesAuthTest(TestCase):
    """
    Checking the health of the connection and authorization with obtaining a
    token for working with the remote service API.
    """
    @classmethod
    def setUpTestData(cls):
        """
        setUpTestData: Run once to set unmodified data for all class methods.
        """
        pass

    def setUp(self):
        """
        setUp: Run once for each test method, to set up clean data.
        """
        # self.mock_get_patcher = patch('src.cloudtipsadp.adp.requests.get')
        self.mock_post_patcher = patch('src.cloudtipsadp.adp.requests.post')
        # self.mock_get = self.mock_get_patcher.start()
        self.mock_post = self.mock_post_patcher.start()

    def tearDown(self):
        # self.mock_get_patcher.stop()
        self.mock_post_patcher.stop()

    def test_request_response(self):
        """Checking the connection of the service to the remote API."""
        response = cta.get_token(self)
        self.assertIsNotNone(response)

    def test_getting_cloudtips(self):
        """Connecting to a remote server will return True."""
        self.mock_post.return_value.ok = True
        response = cta.get_token(self)
        self.assertIsNotNone(response)

    def test_getting_todos_when_response_is_ok(self):
        self.mock_post.return_value.ok = True
        todos = [{
            'access_token': 'vcy56ey3xtw5txe',
            'expires_in': 1659545369,
            'refresh_token': 'vcy56ey3xtw5txe'
        }]

        self.mock_post.return_value = Mock()
        self.mock_post.return_value.json.return_value = todos
        response = cta.get_token(self)
        self.assertEqual(response.json(), todos)
