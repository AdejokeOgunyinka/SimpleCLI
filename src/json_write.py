import json
from src.fetch_data_to_write import FetchData


class Json:
    """This class has a static method which is responsible for writing a python dictionary into a json file."""
    @staticmethod
    def write_json(list_of_keys):
        data = FetchData.get_from_data_file(list_of_keys)
        # The code below is used to add information from the list to the csv file, including the headers as well
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
