from unittest import TestCase


class TestTStrings(TestCase):
    def test_hello_tstring(self):
        tHello = t'Hello, {world}!'
        print(tHello)
