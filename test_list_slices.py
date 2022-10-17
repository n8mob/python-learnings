from unittest import TestCase


class TestListSlices(TestCase):
    def setUp(self) -> None:
        self.a_list = [0, 1, 2, 3, 4, 5]

    def test_left_slice(self):
        expected = [0, 1, 2]

        actual = self.a_list[:3]

        self.assertEqual(expected, actual)

    def test_right_slice(self):
        expected = [3, 4, 5]

        actual = self.a_list[3:]

        self.assertEqual(expected, actual)
