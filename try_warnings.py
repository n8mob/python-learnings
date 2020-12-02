import warnings
from unittest import TestCase


def do_not_foo():
    warnings.warn('We should always foo in the new way', DeprecationWarning)
    return "Old foo"


def different_foo():
    warnings.warn('Nonspecific warning')
    return "Weird foo"


def new_foo():
    return "New foo"


def future_feature_foo():
    warnings.warn('This feature will go away soon. If you really need it file a bug report.', FutureWarning)
    return "Outdated user foo"


class TestFoos(TestCase):

    def test_old_foo(self):
        actual = do_not_foo().lower()

        self.assertIn('old', actual)
        self.assertIn('foo', actual)

    def test_new_foo(self):
        actual = new_foo().lower()

        self.assertIn('new', actual)
        self.assertIn('foo', actual)

    def test_different_foo(self):
        actual = different_foo().lower()

        self.assertIn('weird', actual)
        self.assertIn('foo', actual)


if __name__ == "__main__":
    print(f'Main says:\n')
    print(new_foo())
    print(do_not_foo())
    print('Loop over code that warns')

    for i in range(5):
        print(f'{i}: {different_foo()}')

    print(future_feature_foo())
