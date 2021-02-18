from unittest import TestCase

KEY1 = 'key1'
KEY2 = 'key2'
KEY3 = 'key3'

VALUE2 = 'value2'


class TestDictionaryKeys(TestCase):
    def setUp(self) -> None:
        self.non_empty_dict = {
            KEY1: 'value1',
            KEY2: VALUE2,
        }

    def test_key_in_dictionary(self):
        self.assertTrue(KEY1 in self.non_empty_dict)
        self.assertIn(KEY2, self.non_empty_dict)

    def test_key_not_in_dictionary(self):
        self.assertFalse('not' in self.non_empty_dict)
        self.assertNotIn('not', self.non_empty_dict)

    def test_in_does_not_throw(self):
        try:
            _ = self.non_empty_dict[KEY3]
            self.fail('expecting an exception')
        except KeyError:
            if KEY3 in self.non_empty_dict:
                self.fail(f'"{KEY3}" threw when we indexed on it; it should not count as "in"')

        actual = self.non_empty_dict.get(KEY3)

        self.assertFalse(actual, 'get returns None instead of throwing')
