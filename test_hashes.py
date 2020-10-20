from unittest import TestCase


class TestHashes(TestCase):
    def test_hash_is_int(self):
        actual = hash('abc')

        self.assertIsInstance(actual, int)

    def test_hashes_are_equal(self):
        s1 = 'abc'
        s2 = 'ABC'.lower()

        self.assertEqual(s1, s2)
        self.assertIsNot(s1, s2)

        h1 = hash(s1)
        h2 = hash(s2)

        self.assertEqual(h1, h2)
