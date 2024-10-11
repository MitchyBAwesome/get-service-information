import unittest
from unittest.mock import patch, MagicMock
from src.aws_service_explorer import get_service_list, choose_service, get_api_actions

class TestAWSServiceExplorer(unittest.TestCase):

    @patch('src.aws_service_explorer.requests.get')
    def test_get_service_list(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '[{"service": "TestService", "url": "http://test.com"}]'
        mock_get.return_value = mock_response

        result = get_service_list()
        self.assertEqual(result, [{"service": "TestService", "url": "http://test.com"}])

    @patch('builtins.input', return_value='TestService')
    def test_choose_service(self, mock_input):
        services = [{"service": "TestService", "url": "http://test.com"}]
        result = choose_service(services)
        self.assertEqual(result, {"service": "TestService", "url": "http://test.com"})

    @patch('src.aws_service_explorer.requests.get')
    def test_get_api_actions(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '{"Actions": [{"Name": "TestAction"}]}'
        mock_get.return_value = mock_response

        result = get_api_actions("http://test.com")
        self.assertEqual(result, ["TestAction"])

if __name__ == '__main__':
    unittest.main()