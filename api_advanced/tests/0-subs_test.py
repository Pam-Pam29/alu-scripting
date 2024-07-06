import unittest
from unittest.mock import patch, Mock
from io import StringIO
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from.. import subs  # Import the subs module

class TestNumberOfSubscribers(unittest.TestCase):
    @patch('requests.get')
    def test_number_of_subscribers(self, mock_get):
        # Mock the response from the Reddit API
        mock_response = Mock()
        mock_response.json.return_value = {'data': {'subscribers': 12345}}
        mock_get.return_value = mock_response

        # Test the function
        self.assertEqual(subs.number_of_subscribers('python'), 12345)

    @patch('requests.get')
    def test_number_of_subscribers_api_error(self, mock_get):
        # Mock an API error response
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        # Test the function
        self.assertEqual(subs.number_of_subscribers('python'), 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        # Test the main function
        sys.argv = ['0-main.py', 'python']
        with patch('subs.number_of_subscribers') as mock_number_of_subscribers:
            mock_number_of_subscribers.return_value = 12345
            with open('../0-main.py') as f:
                code = compile(f.read(), '../0-main.py', 'exec')
                exec(code, globals(), locals())
            self.assertEqual(mock_stdout.getvalue().strip(), '12345')

if __name__ == '__main__':
    unittest.main()
