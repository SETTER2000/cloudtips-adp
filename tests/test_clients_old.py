from unittest import TestCase
from unittest.mock import Mock, patch

from src.cloudtipsadp.clients import Connect


class ClientsTest(TestCase):
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
        # self.mock_get_patcher = patch(
        # 'src.cloudtipsadp.clients.requests.get')
        self.mock_post_patcher = patch(
            'src.cloudtipsadp.clients.requests.post')
        # self.mock_get = self.mock_get_patcher.start()
        self.mock_post = self.mock_post_patcher.start()

    def tearDown(self):
        # self.mock_get_patcher.stop()
        self.mock_post_patcher.stop()

    def test_request_response(self):
        """Checking the connection of the service to the remote API."""
        response = Connect.get_token(self)
        self.assertIsNotNone(response)

    def test_getting_cloudtips(self):
        """Connecting to a remote server will return True."""
        self.mock_post.return_value.ok = True
        response = Connect.get_token(self)
        self.assertIsNotNone(response)

    def test_get_token_ok(self):
        # self.mock_post.return_value = Mock(ok=True)
        self.mock_post.return_value.ok = True
        # self.mock_post.return_value.access_token = 'werte56tefrqw3r'

        todos = [{
            'access_token': 'vcy56ey3xtw5txe',
            'expires_in': 1800,
            'token_type': 'Bearer',
            'refresh_token': 'vcy56ey3xtw5txe',
            'scope': 'api email IdentityAPI offline_access openid phone prof'
        }]

        self.mock_post.return_value = Mock()
        self.mock_post.return_value.json.return_value = todos
        response = Connect.get_token(self)
        self.assertEqual(response.json(), todos)
