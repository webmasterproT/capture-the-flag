import unittest
from unittest.mock import patch
from utils.osint_utils import gather_intelligence, search_social_media
from osint import OSINTHandler

class TestOSINT(unittest.TestCase):
    def setUp(self):
        self.osint_handler = OSINTHandler(api_key='your_api_key_here')

    @patch('utils.osint_utils.gather_intelligence')
    def test_gather_intelligence(self, mock_gather_intelligence):
        test_query = "test_query"
        expected_result = {'data': 'some_intelligence_data'}
        mock_gather_intelligence.return_value = expected_result

        result = self.osint_handler.gather_intelligence(test_query)
        self.assertEqual(result, expected_result)
        mock_gather_intelligence.assert_called_once_with(test_query)

    @patch('utils.osint_utils.search_social_media')
    def test_search_social_media(self, mock_search_social_media):
        test_platform = "twitter"
        test_query = "test_handle"
        expected_result = {'tweets': ['tweet1', 'tweet2']}
        mock_search_social_media.return_value = expected_result

        result = self.osint_handler.search_social_media(test_platform, test_query)
        self.assertEqual(result, expected_result)
        mock_search_social_media.assert_called_once_with(test_platform, test_query)

    def test_invalid_api_key(self):
        with self.assertRaises(ValueError):
            OSINTHandler(api_key='')

    def test_invalid_search_parameters(self):
        with self.assertRaises(ValueError):
            self.osint_handler.search_social_media("", "")

if __name__ == '__main__':
    unittest.main()