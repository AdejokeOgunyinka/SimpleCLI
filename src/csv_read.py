class CsvReader:
    """This class has a static method which is responsible for reading from the csv file that was created."""
    @staticmethod
    def read():
        with open('data.csv') as reader:
            return reader.readlines()
