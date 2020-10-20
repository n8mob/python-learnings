from unittest import TestCase


class TestIntegerParsing(TestCase):
    def test_1(self):
        self.assertEqual(1, int('1'))

    def test_minus1(self):
        self.assertEqual(-1, int('-1'))

    def test_zero(self):
        self.assertEqual(0, int('0'))

    def test_signed_int32_max_minus1(self):
        self.assertEqual(2147483646, int('2147483646'))

    def test_signed_int32_max(self):
        self.assertEqual(2147483647, int('2147483647'))

    def test_signed_int32_max_plus1(self):
        self.assertEqual(2147483648, int('2147483648'))

    def test_signed_int64_max_minus1(self):
        self.assertEqual(9223372036854775806, int('9223372036854775806'))

    def test_signed_int64_max(self):
        self.assertEqual(9223372036854775807, int('9223372036854775807'))

    def test_signed_int64_max_plus1(self):
        self.assertEqual(9223372036854775808, int('9223372036854775808'))

    def test_int_of_int(self):
        self.assertEqual(1, int(1))
        self.assertEqual(6283, int(6283))
