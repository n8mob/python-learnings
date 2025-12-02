from unittest import TestCase

class TestModeOperator(TestCase):
    def test_is_mod_max_inclusive(self):
        mod_value = 99
        self.assertEqual(1, 100 % mod_value, 'I would expect 100 % 99 to be 1')

    def test_is_mod_zero(self):
        mod_value = 100
        self.assertEqual(0, 100 % mod_value, 'I would expect 100 % 100 to be 0')

    def test_is_mod_below_zero(self):
        mod_value = 100
        self.assertEqual(99, -1 % mod_value, 'I would expect -1 % 100 to be 99')

    def test_mod_with_self_is_zero(self):
        mod_value = 100
        self.assertEqual(0, 100 % mod_value, 'I would expect 0 % 100 to be 0')

    def test_mod_within_bounds(self):
        mod_value = 100
        self.assertEqual(42, 42 % mod_value, 'I would expect 42 % 100 to be 42')

    def test_mod_negative_within_bounds(self):
        mod_value = 100
        self.assertEqual(58, -42 % mod_value, 'I would expect -42 % 100 to be 58')
