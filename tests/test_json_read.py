import unittest
import os
from src.json_read import JsonReader
from src.json_write import Json


class JsonReadTest(unittest.TestCase):
    def setUp(self) -> None:
        self.exec = lambda list_of_keys: Json.write_json(list_of_keys)

    def test_json_writes(self):
        self.assertEqual(self.exec(['python', 'java']), None)
        output = [{'oop': True, 'popularity': 9, 'extension': 'py'}, {'oop': True, 'popularity': 7, 'extension': 'java'}]
        self.assertEqual(JsonReader.read(), output)

    def test_correct_keys(self):
        self.assertEqual(self.exec(['javascript', 'golang', 'php']), None)
        result = [{'oop': True, 'popularity': 10, 'extension': 'js'},
                  {'oop': False, 'popularity': 4, 'extension': 'go'},
                  {'oop': True, 'popularity': 10, 'extension': 'php'}]
        read = JsonReader.read()
        self.assertEqual(read, result)

    def tearDown(self) -> None:
        if os.path.exists('../tests/data.json'):
            os.remove('../tests/data.json')


if __name__ == "__main__":
    unittest.main()
