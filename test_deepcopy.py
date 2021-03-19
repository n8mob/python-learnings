from copy import deepcopy
from unittest import TestCase


class TestDeepcopy(TestCase):
    def test_simple_dict(self):
        source = {
            'a': 'b',
            'c': 'd',
        }

        dest = source.copy()

        self.assertEqual(source, dest)

    def test_simple_deepcopy(self):
        source = {
            'a': 'b',
            'c': 'd',
        }

        dest = deepcopy(source)

        self.assertEqual(source, dest)

    def test_modify_after_shallow_copy(self):
        source = {
            'a': 'b',
            'c': 'd',
        }

        dest = source.copy()

        dest['a'] = 'e'

        self.assertEqual('e', dest['a'])
        self.assertNotEqual('e', source['a'])

    def test_modify_after_deep_copy(self):
        source = {
            'a': 'b',
            'c': 'd',
        }

        dest = deepcopy(source)

        dest['a'] = 'e'

        self.assertEqual('e', dest['a'])
        self.assertNotEqual('e', source['a'])

    def test_complex_dict(self):
        source = {
            'a': {
                'b': 'c',
                'd': 'e',
            },
            'f': {
                'g': 'h',
                'i': 'j',
            }
        }

        dest = source.copy()

        self.assertEqual(source, dest)

        dest['a']['b'] = 'k'

        self.assertEqual('k', source['a']['b'])
        self.assertEqual(source['a']['b'], dest['a']['b'])

    def test_str_operations(self):
        source = {
            'a': 'b',
        }

        dest = source.copy()

        dest['a'].replace('b', 'c')

        self.assertEqual(source, dest)

        dest['a'] = dest['a'].upper()

        self.assertNotEqual(source['a'], dest['a'])
        self.assertEqual('B', dest['a'])
        self.assertNotEqual('B', source['a'])
