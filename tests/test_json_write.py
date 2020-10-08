import unittest
import os
from src.json_read import JsonReader
from src.json_write import Json
from src.file_exists import does_file_exist


class TestWriteJson(unittest.TestCase):
    """This json test class tests if the json function writes, what happens when the correct keys & wrong keys are input \
    and if the file is created"""
    def setUp(self) -> None:
        self.exec = lambda list_of_keys: Json.write_json(list_of_keys)

    def test_json_writes(self):
        self.assertEqual(self.exec(['python', 'java']), None)

    def test_correct_keys(self):
        self.assertEqual(self.exec(['javascript', 'golang', 'php']), None)

    def test_wrong_keys(self):
        with self.assertRaises(KeyError):
            self.assertEqual(self.exec(['jav', 'gol', 'pea']), None)
        with self.assertRaises(KeyError):
            self.assertEqual(self.exec(['1', '2']), None)

    def test_file_creation(self):
        self.assertEqual(self.exec(['javascript', 'php', 'golang']), None)
        self.assertEqual(does_file_exist('../tests/data.json'), True)

    def tearDown(self) -> None:
        if os.path.exists('../tests/data.json'):
            os.remove('../tests/data.json')


if __name__ == "__main__":
    unittest.main()
