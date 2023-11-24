import unittest
from unittest.mock import patch
from what_year import what_is_year_now
import io


class TestWhatYearNow(unittest.TestCase):
    """Testing function what_is_year_now() from what_is_year_now.py"""

    def test_ymd_format(self):
        """
        Test that checks the behavior of a function in the format YYYY-MM-DD
        """
        to_json = '{"currentDateTime" : "2023-10-30"}'
        with patch('urllib.request.urlopen') as mocked_object:
            mocked_object.return_value = io.StringIO(to_json)
            actual = what_is_year_now()
            expected = 2023
            self.assertEqual(actual, expected)
            mocked_object.assert_called_once()

    def test_dmy_format(self):
        """
        Test that checks the behavior of a function in the format DD.MM.YYYY
        """
        to_json = '{"currentDateTime" : "30.10.2023"}'
        with patch('urllib.request.urlopen') as mocked_object:
            mocked_object.return_value = io.StringIO(to_json)
            actual = what_is_year_now()
            expected = 2023
            self.assertEqual(actual, expected)
            mocked_object.assert_called_once()

    def test_incorrect_format(self):
        """
        Test that checks the behavior of a function in the format: DD?MM?YYYY
        """
        to_json = '{"currentDateTime" : "30?10?2023"}'
        with patch('urllib.request.urlopen') as mocked_object:
            mocked_object.return_value = io.StringIO(to_json)
            with self.assertRaises(ValueError):
                what_is_year_now()
