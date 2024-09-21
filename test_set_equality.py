from unittest import TestCase


class TestSetEquality(TestCase):
  def test_1(self):
    list1 = [1, 2, 3]
    list2 = [3, 2, 1]
    set1 = set(list1)
    set2 = set(list2)

    self.assertNotEqual(list1, list2)
    self.assertEqual(set1, set2)

  def test_empty_set(self):
    empty_set = set()
    set_from_empty_list = set([])

    self.assertEqual(set_from_empty_list, empty_set)

  def test_subset_equality(self):
    set1: set = {1, 2}
    set2 = {1}
    self.assertNotEquals(set1, set2)
    set2.add(2)
    self.assertEqual(set1, set2)

  def test_set_of_sets(self):
    f1 = frozenset({1})
    f2 = frozenset({2})
    f3 = frozenset({3})
    f4 = frozenset({4})

    set1 = {f1, f2}
    set2 = {f3, f4}

    self.assertNotEqual(set1, set2)

    set1.add(f3)
    set1.add(f4)

    self.assertNotEqual(set1, set2)

    set2.add(f1)
    set2.add(f2)

    self.assertEqual(set1, set2)

  def test_set_including_empty_set(self):
    f1 = frozenset({1})
    f2 = frozenset({2})
    f3 = frozenset()

    set1 = {f1, f2}
    set2 = {f1, f2}

    self.assertEqual(set1, set2)

    set1.add(f3)
    set2.add(f3)

    self.assertEqual(set1, set2)
