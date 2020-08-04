import base64
from unittest import TestCase


class TestBase64RoundTrip(TestCase):

    def test_bytes(self):
        abc = "ABC"

        abc_bin = abc.encode('utf-8')
        self.assertIsInstance(abc_bin, bytes)
        self.assertIn(0x41, abc_bin)
        self.assertIn(0x42, abc_bin)
        self.assertIn(0x43, abc_bin)

        expected_b64 = b'QUJD'
        abc_b64_default = base64.b64encode(abc_bin)
        abc_b64_explicit = base64.b64encode(abc.encode('utf-8'))

        self.assertEqual(abc_b64_explicit, abc_b64_default)

        self.assertEqual(expected_b64, abc_b64_explicit)

        d = base64.b64decode(abc_b64_explicit)

        self.assertIsInstance(d, bytes)

        self.assertEqual(abc_bin, d)
