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

        self.assertEqual(actual1, 'test_key1')
        self.assertEqual(actual2, 'test_key2')

        with self.assertRaises(ValueError) as vex_context:
            key1, value1, key2, value2 = d
            self.assertIsNone(key1)
            self.assertIsNone(value1)
            self.assertIsNone(key2)
            self.assertIsNone(value2)

        actual = str(vex_context.exception)

        self.assertIn('not enough', actual)
        self.assertIn('expected 4, got 2', actual)
