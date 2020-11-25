from datetime import datetime
from unittest import TestCase


class TestDateParsing(TestCase):
    def test_iso_format(self):
        string = '2020-12-31 12:00:00'

        actual = datetime.fromisoformat(string)
        expected = datetime(2020, 12, 31, 12)

        self.assertEqual(expected, actual)

    def test_another_string(self):
        string = '2019-12-04 10:50:20'

        actual = datetime.fromisoformat(string)
        expected = datetime(2019, 12, 4, 10, 50, 20)

        self.assertEqual(expected, actual)
