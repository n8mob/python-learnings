from unittest import TestCase

KEY1 = 'key1'
KEY2 = 'key2'
KEY3 = 'key3'

EMPTY_LIST = []
VALUE2 = 'value2'


class TestDictionary(TestCase):
  def setUp(self) -> None:
    self.non_empty_dict = {
      KEY1: EMPTY_LIST,
      KEY2: VALUE2,
    }

  def test_key_in_dictionary(self):
    self.assertTrue(KEY1 in self.non_empty_dict)
    self.assertIn(KEY2, self.non_empty_dict)

  def test_key_not_in_dictionary(self):
    self.assertFalse('not' in self.non_empty_dict)
    self.assertNotIn('not', self.non_empty_dict)

  def test_in_does_not_throw(self):
    try:
      _ = self.non_empty_dict[KEY3]
      self.fail('expecting an exception')
    except KeyError:
      if KEY3 in self.non_empty_dict:
        self.fail(f'"{KEY3}" threw when we indexed on it; it should not count as "in"')

    actual = self.non_empty_dict.get(KEY3)

    self.assertFalse(actual, 'get returns None instead of throwing')

  def test_empty_list_is_in(self):
    self.assertIn(KEY1, self.non_empty_dict, 'value is empty, but the key should be in there')

  def test_insert_new_key(self):
    self.assertNotIn(KEY3, self.non_empty_dict, 'KEY3 not in dictionary is a pre-condition for this test')

    test_value = "test"
    self.non_empty_dict[KEY3] = test_value

    self.assertIn(KEY3, self.non_empty_dict, 'KEY3 should now be in the dictionary')
    self.assertEqual(test_value, self.non_empty_dict[KEY3], 'KEY3 should map to the test value')

  def test_empty_dicts_are_equal(self):
    dictA: dict = {}
    dictB: dict = {}
    self.assertTrue(dictA == dictB)

  def test_one_item_are_equal(self):
    dictA: dict = {KEY1: 'value1'}
    dictB: dict = {KEY1: 'value1'}

    self.assertTrue(dictA == dictB)

  def test_two_items_are_equal(self):
    dictA: dict = {KEY1: 'value1', KEY2: 'value2'}
    dictB: dict = {KEY1: 'value1', KEY2: 'value2'}
    self.assertTrue(dictA == dictB)

  def test_two_items_out_of_order(self):
    dictA: dict = {KEY1: 'value1', KEY2: 'value2'}
    dictB: dict = {KEY2: 'value2', KEY1: 'value1'}

    self.assertEqual(dictA, dictB)

    self.assertTrue(dictA == dictB)

  def test_equality_reflects_changs(self):
    dictA: dict = {KEY1: 'value1', KEY2: 'value2'}
    dictB: dict = {}

    self.assertNotEquals(dictA, dictB)

    dictB[KEY1] = 'value1'
    self.assertNotEquals(dictA, dictB)

    dictB[KEY2] = 'value2'
    self.assertEqual(dictA, dictB)

    dictA[KEY3] = 'value3'
    self.assertNotEquals(dictA, dictB)

    dictA.pop(KEY3)
    self.assertEqual(dictA, dictB)

  def test_equality_of_values(self):
    dictA: dict = {KEY1: 'value1', KEY2: 'value2'}
    dictB: dict = {KEY1: 'value3', KEY2: 'value4'}

    self.assertNotEquals(dictA, dictB)

    dictB[KEY1] = 'value1'
    self.assertNotEquals(dictA, dictB)

    dictB[KEY2] = 'value2'
    self.assertEqual(dictA, dictB)

  def test_equality_of_keys(self):
    dictA: dict = {KEY1: 'value1', KEY2: 'value2'}
    dictB: dict = {KEY1: 'value3', KEY2: 'value4'}

    self.assertEqual(dictA.keys(), dictB.keys())
    self.assertNotEquals(dictA, dictB)
