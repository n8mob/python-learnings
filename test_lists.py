from unittest import TestCase


class TestLists(TestCase):
    def test_empty_error(self):
        empty_list = []

        with self.assertRaises(IndexError):
            _ = empty_list[0]

    def test_unpack_a_long_list(self):
        long_list = [1, 2, 3, 4, 5]

        first, *rest = long_list

        self.assertEqual(1, first)
        self.assertEqual(2, rest[0])
