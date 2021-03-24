from unittest import TestCase


class TestLists(TestCase):
    def test_empty_error(self):
        empty_list = []

        with self.assertRaises(IndexError):
            _ = empty_list[0]
