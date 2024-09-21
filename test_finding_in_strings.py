import unittest


class TestFindingInStrings(unittest.TestCase):
  def test_find_when_found(self):
    s = 'Hello, World!'
    self.assertEqual(7, s.find('W'))

  def test_index_of_when_found(self):
    s = 'Hello, World!'
    self.assertEqual(7, s.index('W'))

  def test_find_when_not_found(self):
    s = 'Hello, World!'
    self.assertEqual(-1, s.find('Python'))

  def test_index_of_when_not_found(self):
    s = 'Hello, World!'
    with self.assertRaises(ValueError):
      s.index('Python')


if __name__ == '__main__':
  unittest.main()
