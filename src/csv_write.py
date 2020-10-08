import csv
from src.fetch_data_to_write import FetchData


class Csv:
    """This class has a static method which is responsible for writing a python dictionary into a csv file."""
    # The code below is used to add information from the list to the csv file, including the headers as well

    @staticmethod
    def write_csv(key_list):
        data = FetchData.get_from_data_file(key_list)
        with open('data.csv', 'w', newline='') as file:
            headers = ['oop', 'popularity', 'extension']
            write = csv.DictWriter(file, fieldnames=headers)
            write.writeheader()
            write.writerows(data)

