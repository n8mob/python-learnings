from unittest import TestCase


class TestChainedInequalities(TestCase):
    def test_ints(self):
        self.assertTrue(0 <= 1, 'simple 1')
        self.assertTrue(1 <= 2, 'simple 2')
        self.assertTrue(0 <= 1 <= 2, 'not so simple')
        self.assertFalse(2 <= 1, 'simple 3')
        self.assertFalse(2 <= 1 <= 0, 'very unsimple')

    def test_strings(self):
        self.assertTrue('a' < 'b')
        self.assertTrue('b' > 'a')
        self.assertTrue('B' > 'A')
        self.assertTrue('b' > 'A', 'big A')
        self.assertTrue('A' < 'Z' < 'a', 'holy moley!')
