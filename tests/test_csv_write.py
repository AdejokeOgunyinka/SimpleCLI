import unittest
import os
from src.csv_read import CsvReader
from src.csv_write import Csv
from src.file_exists import does_file_exist


class CsvWriteTest(unittest.TestCase):

    """This csv test class tests if the csv function writes, what happens when the correct keys & wrong keys are input
    and if the file is created"""
    def setUp(self) -> None:
        self.exec = lambda list_of_keys: Csv.write_csv(list_of_keys)

    def test_csv_writes(self):
        self.assertEqual(self.exec(['python', 'java']), None)

    def test_correct_keys(self):
        self.assertEqual(self.exec(['javascript', 'golang', 'php']), None)

    def test_wrong_keys(self):
        with self.assertRaises(KeyError):
            self.assertEqual(self.exec(['jav', 'gol', 'pea']), None)
        with self.assertRaises(KeyError):
            self.assertEqual(self.exec(['1', '2']), None)

    def test_file_creation(self):
        self.assertEqual(self.exec(['golang', 'javascript', 'php']), None)
        self.assertEqual(does_file_exist('../tests/data.csv'), True)

    def tearDown(self) -> None:
        if os.path.exists('../tests/data.csv'):
            os.remove('../tests/data.csv')


if __name__ == "__main__":
    unittest.main()
