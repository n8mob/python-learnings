import unittest


class TestWhenVariableNotDefined(unittest.TestCase):
    def test_nonexistent_variable(self):
        try:
            if nonexistent:
                self.fail('nonexistent variable is defined')
        except UnboundLocalError as e:
            self.assertIsNotNone(e)

        nonexistent = 'now defined'

        if not nonexistent:
            self.fail('nonexistent variable is still not defined')
