import unittest
from unittest.mock import patch
from api_interaction import send_api_request, receive_api_response

class TestAPIInteraction(unittest.TestCase):

    @patch('api_interaction.send_api_request')
    def test_send_api_request(self, mock_send_api_request):
        test_api_key = 'test_api_key'
        test_payload = {'action': 'test_action'}
        send_api_request(test_api_key, test_payload)
        mock_send_api_request.assert_called_with(test_api_key, test_payload)

    @patch('api_interaction.receive_api_response')
    def test_receive_api_response(self, mock_receive_api_response):
        test_response_data = {'result': 'success'}
        mock_receive_api_response.return_value = test_response_data
        response = receive_api_response()
        self.assertEqual(response, test_response_data)

if __name__ == '__main__':
    unittest.main()