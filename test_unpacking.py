from unittest import TestCase


class TestUnpacking(TestCase):
    def test_unpack_tuple(self):
        t = 'two', 'values'

        actual1, actual2 = t

        self.assertEqual('two', actual1)
        self.assertEqual('values', actual2)

    def test_unpack_dictionary(self):
        d = {
            'test_key1': 'test_dict_value1',
            'test_key2': 'test_dict_value2',
        }

        actual1, actual2 = d

        self.assertEqual(actual1, 'test_dict_value1')
        self.assertEqual(actual2, 'test_dict_value2')
