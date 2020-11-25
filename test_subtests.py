from unittest import TestCase


'''
class MyTests(unittest.TestCase):
    def test_bad_validation(self):
        for test_dict in (
                {},
                {'a':1},
                {'b':2, 'else':3},
                {'special_key':4},
                ):
            with self.subTest(test_dict=test_dict):
                with self.assertRaises(Exception) as context:
                    MyClass(test_dict)
                self.assertTrue('Unable to create' in str(context.exception))
'''


test_cases = [
    {'a': 1, 'b': 2},
    {'a': 2, 'b': 4},
]


class TestSubtests(TestCase):
    def test_two_subtests(self):
        for test_dict in test_cases:
            with self.subTest(test_dict):
                self.assertEqual(test_dict['a'] * 2, test_dict['b'])
