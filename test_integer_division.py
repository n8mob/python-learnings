from unittest import TestCase


class TestIntegerDivision(TestCase):
    def test_simple_cases(self):
        self.assertEqual(1, 7 % 3)
        self.assertEqual(2, 7 // 3)
        self.assertEqual(1, 100 // 100, 'I would expect 100 // 100 to be 1')
        self.assertEqual(1, 101 // 100)

    def test_with_negative(self):
        self.assertEqual(0, 1 // 100, 'I would expect 1 // 100 to be 0')
        # I would expect -1 // 100 to be 0
        # but `//` is not truncating ("truncating toward zero", more specificly)
        # it's actualy "floor division", meaning, it always rounds down.
        # so for negatives, it ends up one lower than I thought.
        self.assertEqual(-1, -1 // 100, 'I would expect -1 // 100 to be 0')
        self.assertEqual(0, int(-1 / 100))
