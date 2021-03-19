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
