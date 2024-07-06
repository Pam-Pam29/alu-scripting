import unittest
from unittest.mock import patch
from io import StringIO
from your_module import number_of_subscribers  # Replace 'your_module' with the actual name of the module where the function is defined

class TestNumberOfSubscribers(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_number_of_subscribers(self, mock_stdout):
        number_of_subscribers()
        self.assertEqual(mock_stdout.getvalue().strip(), '42')

if __name__ == '__main__':
    unittest.main()
