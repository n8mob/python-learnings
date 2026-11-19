from unittest import TestCase
from unittest.mock import Mock


class TestMocks(TestCase):
    def test_simple_mock(self):
        mocker = Mock()
        mocker.call1.return_value = "mock1"

        self.assertEqual(mocker.call1.call_count, 0)

        actual = mocker.call1()

        self.assertEqual(mocker.call1.call_count, 1)

        self.assertEqual("mock1", actual)

    def test_last_return_wins(self):
        mocker = Mock()
        mocker.call1.return_value = "mock1"
        mocker.call1.return_value = "mock2"

        actual1 = mocker.call1()

        self.assertEqual("mock2", actual1)

        actual2 = mocker.call1()

        self.assertEqual("mock2", actual2)

    def test_sequence_return(self):
        mocker = Mock()
        mocker.call1.return_value = "never returns"
        mocker.call1.side_effect = ["mock1", "mock2", "mock3"]

        actual1 = mocker.call1()
        actual2 = mocker.call1()
        actual3 = mocker.call1()
        self.assertEqual(mocker.call1.return_value, "never returns")

        try:
            _ = mocker.call1()
            self.fail("Should have thrown an error")
        except StopIteration as e:
            print(e)
            self.assertEqual(mocker.call1.return_value, "never returns")

        self.assertEqual("mock1", actual1)
        self.assertEqual("mock2", actual2)
        self.assertEqual("mock3", actual3)
