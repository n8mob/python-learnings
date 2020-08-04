from unittest import TestCase


def return_kwargs_as_dict(**kwargs):
    return {k: kwargs[k] for k in kwargs}


class TestKwargs(TestCase):
    def test_parameter_name_in_dictionary(self):
        actual = return_kwargs_as_dict(foo='bar')
        self.assertTrue(actual)
        self.assertIn('foo', actual)
        self.assertEqual('bar', actual['foo'])
