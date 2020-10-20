import tempfile
from unittest import TestCase


class TestOpeningFiles(TestCase):

    # bad argument is the point of this test
    # noinspection PyTypeChecker
    def test_none_file(self):
        with self.assertRaises(TypeError):
            open(None)

    def test_empty_string_filename(self):
        with self.assertRaises(FileNotFoundError):
            open('')

    def test_missing_file(self):
        random_filename = tempfile.NamedTemporaryFile().name
        with self.assertRaises(FileNotFoundError):
            open(random_filename)

    def test_reading_empty_file(self):
        actual = open('empty_file.txt')
        self.assertFalse(actual.read())
