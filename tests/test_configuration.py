from unittest import TestCase

from src.cloudtipsadp.configuration import Configuration


class ConfigurationTest(TestCase):
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
        self.conf = Configuration

    def test_constants_file(self):
        """Проверка аналогичности тестового и рабочего файла констант."""
        # self.assertEqual('tests/test_configuration.py',
        #                  'src/cloudtipsadp/configuration.py')
        pass

    # @pytest.mark.parametrize('a, result', [('234wererter', '234wererter')])
    # def test_configure_auth_token_ok(self, a, result):
    #     # self.conf.configure_auth_token(a)
    #     # self.assertEqual(self.conf.auth_token, result)
    #     pass
    #
    # @pytest.mark.parametrize('a, result', [('234wererter', '234wererter')])
    # def test_configure_auth_token_error(self, a, result, *args, **kwarg):
    #     pass
