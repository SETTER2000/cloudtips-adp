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
        self.g = 100

    def test_smoke(self):
        """Smoke test."""
        self.assertEqual(self.g, 100)

    def test_smoke2(self):
        """Smoke test 2."""
        self.assertEqual(self.g, 100)


