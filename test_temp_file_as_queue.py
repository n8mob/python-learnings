import io
import tempfile
from unittest import TestCase


class TestTempFileAsQueue(TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryFile()
        self.text = io.TextIOWrapper(temp)

    def tearDown(self) -> None:
        self.text.close()

    def test_file_looks_as_expected(self):
        self.assertTrue(self.text.writable(), 'file should be writable')
        self.assertTrue(self.text.readable(), 'file should be readable')
        self.assertTrue(self.text.seekable(), "I expect we'll need to seek")

    def test_write(self):
        self.text.write('hello')

    def test_write_then_read(self):
        self.text.write('a')
        self.text.seek(0)
        actual = self.text.read(1)
        self.assertTrue(actual, 'expecting to read a single byte')
        self.assertEqual('a', actual)
