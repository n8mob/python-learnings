import unittest


class TestCasefold(unittest.TestCase):
    def test_casefold(self):
        up = "BUSSE"
        mix = "Buße"
        self.assertNotEqual(up, mix, 'mixed-case is not equal')
        self.assertEqual(up.upper(), mix.upper(), 'capitalization works pretty well')
        self.assertNotEqual(up.lower(), mix.lower(), 'lower-casing does not')
        self.assertEqual(up.upper().lower(), mix.upper().lower(), 'upper lower')
        self.assertEqual(up.casefold(), mix.casefold(), 'casefold')

        with self.assertRaises(AttributeError) as context:
            None.casefold()

        self.assertIsNotNone(context, "None doesn't have attributes")
        self.assertIsNotNone(context.exception)

        msg = str(context.exception)

        self.assertIn('NoneType', msg)
        self.assertIn('casefold', msg)
