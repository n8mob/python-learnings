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

    # noinspection PyTupleAssignmentBalance
    def test_unpack_none_list(self):
        lst = None

        with self.assertRaises(TypeError) as tex_context:
            a, b = lst
            self.assertIsNone(a)
            self.assertIsNone(b)

        actual = str(tex_context.exception)

        self.assertIn('cannot unpack', actual)
        self.assertIn('NoneType', actual)

    # noinspection PyArgumentList
    def test_append_none(self):
        source_list = None
        destination_list = ['not empty']

        with self.assertRaises(TypeError) as tex_context:
            destination_list.append(*source_list)

        actual = str(tex_context.exception)

        self.assertIn('iterable', actual)
        self.assertIn('NoneType', actual)

        self.assertEqual(['not empty'], destination_list, 'destination list should be unchanged')
