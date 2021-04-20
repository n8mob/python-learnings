import json
from unittest import TestCase

expected_json = '{"a": "a", "b": "b", "c": "c"}'
expected_str = "{'a': 'a', 'b': 'b', 'c': 'c'}"


class CustomObject:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class CustomWithStr(CustomObject):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def __str__(self):
        return str({
            'a': str(self.a),
            'b': str(self.b),
            'c': str(self.c),
        })


class TestJsonNonSerializable(TestCase):
    def setUp(self) -> None:
        self.custom_with_str = CustomWithStr('a', 'b', 'c')
        self.custom_no_str = CustomObject('a', 'b', 'c')

    def test_serialize_custom_object(self):

        with self.assertRaises(TypeError) as error_context:
            json.dumps(self.custom_no_str)

        actual = str(error_context.exception)

        self.assertIn('CustomObject', actual)
        self.assertIn('not JSON serializable', actual)

    def test_with_str(self):

        with self.assertRaises(TypeError) as error_context:
            json.dumps(self.custom_with_str)

        actual = str(error_context.exception)

        self.assertIn('CustomWithStr', actual)

        actual_str = str(self.custom_with_str)

        self.assertEqual(expected_str, actual_str)

    def test_with_dict(self):
        actual = json.dumps(self.custom_with_str.__dict__)

        self.assertEqual(expected_json, actual)

    def test_default_str(self):
        actual = str(self.custom_no_str)

        self.assertIn('CustomObject', actual)
        self.assertIn('object at 0x', actual)
