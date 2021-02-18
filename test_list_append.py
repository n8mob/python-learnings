from unittest import TestCase


class TestListAppend(TestCase):
    def test_flat_map(self):
        a = [1, 2]
        b = [3, 4]
        c = [1, 2, 3, 4]

        self.assertEqual(a + b, c)

    def test_append(self):
        a = [1, 2]
        b = 3
        c = [1, 2, 3]

        a.append(b)

        self.assertEqual(a, c)

    def test_list_add(self):
        a = [1, 2]
        b = [3, 4]
        c = [1, 2, 3, 4]

        self.assertEqual(a + b, c)

    def test_add_empty(self):
        a = [1, 2]
        b = []

        self.assertEqual(a, a + b)

    def test_prepend_list(self):
        a = 1
        b = [2, 3]
        c = [1, 2, 3]

        b.insert(0, a)

        self.assertEqual(b, c)

    def test_unpacking(self):
        a = 1
        b = [2, 3]
        c = [1, 2, 3]

        d = [a, *b]

        self.assertEqual(c, d)

    def test_concat_none(self):
        a = None
        b = [1, 2]

        actual = a or [] + b

        self.assertEqual(b, actual)
