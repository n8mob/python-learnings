from unittest import TestCase


class TestGetAttr(TestCase):
    def test_when_attribute_does_not_exist(self):
        unit_under_test = {}
        with self.assertRaises(AttributeError):
            getattr(unit_under_test, 'foo')

    def test_when_attribute_exists_but_is_missing(self):
        class Foo(object):
            def __init__(self):
                self.bar = None

        actual = getattr(Foo(), 'bar')
        self.assertEqual(actual, None) # but we explicitly set it to None in __init__...

    def test_no_raise_version(self):
        class Foo(object):
            def __init__(self):
                self.bar = None

        with self.assertRaises(AttributeError):
            getattr(Foo(), 'baz')

        actual = getattr(Foo(), 'quux', None)

        self.assertIsNone(actual)
