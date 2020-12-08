from unittest import TestCase

KEY2 = 'key2'

KEY1 = 'key1'


class TestKeyInDictionary(TestCase):
    def setUp(self) -> None:
        self.non_empty_dict = {
            KEY1: 'value1',
            KEY2: 'value2',
        }

    def test_key_in_dictionary(self):
        self.assertTrue(KEY1 in self.non_empty_dict)
        self.assertIn(KEY2, self.non_empty_dict)

    def test_key_not_in_dictionary(self):
        self.assertFalse('not' in self.non_empty_dict)
        self.assertNotIn('not', self.non_empty_dict)
