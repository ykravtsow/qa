import sys
sys.path.append('.')
import requests
import unittest
from unittest.mock import patch
import get_responce


class RequestsTests(unittest.TestCase):
    def test_original(self):
        responce=get_responce.get_responce()
        self.assertTrue(responce is not None)
        print(responce.status_code)
        print(responce.headers)
        print(responce.text)

    @patch('get_responce.get_responce', create=True)
    def test_requests_status_code(self, mock_get):
        mock_get.return_value.status_code = 280
        responce=get_responce.get_responce()
        self.assertTrue(responce.status_code is 280)

    @patch('get_responce.get_responce', create=True)
    def test_requests_responce(self, mock_get):
        print(mock_get.return_value.__dir__())
        mock_get.return_value.status_code = 280
        mock_get.return_value.headers={'Accept':'*'}
        mock_get.return_value.text='<html><head></head><body>test</body></html>'
        responce=get_responce.get_responce()
        print(responce.text)
        self.assertTrue(responce is not None)


if __name__ == 'main':
    unittest.main()
