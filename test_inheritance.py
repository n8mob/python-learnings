import unittest


class A:
    foo = 'foo in A'


class B(A):
    bar = 'bar in B'


class TestInheritance(unittest.TestCase):
    def test_simple_inheritance(self):
        a = A()
        b = B()

        self.assertEqual(a.foo, b.foo, 'a and b should both have foo')

    def test_assignment_through_subclass(self):
        a = A()
        b = B()

        self.assertEqual(a.foo, b.foo, 'should be equal before assignment')

        b.foo = 'foo assigned to instance of B'

        self.assertNotEqual(a.foo, b.foo, 'should change after')
