from unittest import TestCase


class TestWhileLoops(TestCase):
    def test_expression_after_loop(self):

        count = 0
        while count <= 2:
            self.assertTrue(count <= 2, 'once count is greater than two, the loop should exit')
            count += 1

        self.assertTrue(count >= 2, 'the condition of the loop should be met')
