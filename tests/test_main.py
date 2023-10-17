import unittest
from io import StringIO
from unittest.mock import patch
from src.main import main  # Corrected import path

class TestMain(unittest.TestCase):
    def test_main(self):
        expected_output = 'hello World!\n'

        # Call the function you want to test and capture the return value
        actual_output = main()

        # Assert that the return value matches the expected output
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
