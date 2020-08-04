import unittest


class TestShortCircuit(unittest.TestCase):
    def test_bare_booleans1(self):
        self.assertFalse(True and False)

    def test_bare_booleans2(self):
        self.assertFalse(False and True)

    def test_in_construct(self):
        d = {
            'one': 1,
            'two': 'two',
            'three': None,
        }

        self.assertTrue(d)
        self.assertEqual(3, len(d))
        self.assertTrue(d.__contains__('one'))
        self.assertTrue('two' in d)
        self.assertTrue('three' in d.keys())

        self.assertTrue(True and 'one' in d)
        self.assertTrue('two' in d and True)
        self.assertFalse(False and 'one' in d)
        self.assertFalse('one' in d and False)

        self.assertFalse('four' in d)
        self.assertFalse('four' in d and False)
        self.assertFalse(False and 'four' in d)

        self.assertFalse(False and d['three'])
        self.assertFalse(False and d['four'])
        self.assertFalse(False and d['two'].upper())

        self.assertFalse(False and d['three'].upper())

        self.assertFalse(False and d['four'].upper())

        self.assertFalse('four' in d)

        with self.assertRaises(KeyError) as context:
            d['four'].upper()

        self.assertTrue(context.exception)

        self.assertFalse('four' in d and d['four'])
        self.assertFalse('four' in d and d['four'].upper())
        self.assertFalse('four' in d and d['four'].upper() == 'NONE')
