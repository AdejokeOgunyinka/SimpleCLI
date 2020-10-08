import unittest
import os
from src.csv_read import CsvReader
from src.csv_write import Csv


class CsvReadTest(unittest.TestCase):
    def setUp(self) -> None:
        self.exec = lambda list_of_keys: Csv.write_csv(list_of_keys)

    def test_csv_writes(self):
        self.assertEqual(self.exec(['python', 'java']), None)
        output = ['oop,popularity,extension\n', 'True,9,py\n', 'True,7,java\n']
        self.assertEqual(CsvReader.read(), output)

    def test_correct_keys(self):
        self.assertEqual(self.exec(['javascript', 'golang', 'php']), None)
        result = ['oop,popularity,extension\n', 'True,10,js\n', 'False,4,go\n', 'True,10,php\n']
        read = CsvReader.read()
        self.assertEqual(read, result)

    def tearDown(self) -> None:
        if os.path.exists('../tests/data.csv'):
            os.remove('../tests/data.csv')


if __name__ == "__main__":
    unittest.main()
