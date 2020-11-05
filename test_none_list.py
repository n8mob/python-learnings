import json
from unittest import TestCase


class TestNoneList(TestCase):
    def test_none_list(self):
        expected = json.dumps([])
        actual = json.dumps([None])
        self.assertNotEqual(expected, actual)
