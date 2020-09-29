import json
from unittest import TestCase


class TestEmptyJson(TestCase):
    def test_string_with_empty_json(self):
        actual = json.loads('{}')
        self.assertIsNotNone(actual, 'empty object is not the same as None')
        self.assertFalse(actual, 'empty object is not True')
