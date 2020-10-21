from unittest import TestCase


class TestBooleanParsing(TestCase):
    def test_string_just_like_source_code(self):
        input_true = 'True'
        input_false = 'False'

        self.assertTrue(bool(input_true))
        self.assertTrue(bool(input_false), 'non-empty strings are True')

    def test_compare_bstring(self):
        ss = 'False'
        bs = b'False'

        self.assertTrue(ss, 'non-empty string should be true (even if it says "False")')
        self.assertTrue(bs, 'non-empty bytes should be true if they are non-zero')

        self.assertNotEqual(ss, bs, 'string and bytes do not equate because we do not equate')

        self.assertEqual(bs, ss.encode('utf-8'))
        self.assertEqual(ss, bs.decode('utf-8'))

    def test_zero(self):
        self.assertFalse(bool(0), 'expecting 0 to parse to False')
        self.assertFalse(bool(int("0")), 'expecting int("0") to parse to False')
        self.assertTrue(bool('0'), 'expecting "0" to parse to True')
