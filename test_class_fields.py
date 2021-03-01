from unittest import TestCase


class Foo:
    bar = 'bar'

    def __init__(self, bar):
        self.bar = bar


class TestClassFields(TestCase):
    def test1(self):
        f = Foo(bar='flame')

        self.assertEqual('flame', f.bar, 'instance initialization')
        self.assertEqual('bar', Foo.bar, 'instance variable does not pass through to class')
        self.assertNotEqual(f.bar, Foo.bar, 'expecting different values for instance and class field')
        self.assertNotEqual('flame', Foo.bar, 'expecting class variable to remain unchanged')
