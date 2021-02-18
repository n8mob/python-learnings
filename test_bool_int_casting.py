from unittest import TestCase


class TestBoolIntCasting(TestCase):
    def test_bool_dot_value(self):
        self.assertEqual(1, int(True))
        self.assertEqual(0, int(False))

    def test_bool_has_no_value(self):
        bool_in_question = True

        self.assertFalse(hasattr(bool_in_question, 'value'))
