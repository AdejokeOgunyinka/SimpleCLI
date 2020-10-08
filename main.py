import sys
from src.csv_write import Csv
from src.json_write import Json


if __name__ == "__main__":
    file_format = sys.argv[1]  # save the format from the first argument in the command line, after main.py, in a variable
    key_list = sys.argv[2:]  # save the list of other arguments in a list, since they are the keys to be used.

    # This part of the code checks the format passes in through the command line and passes it to the respective functions to handle
    if len(key_list) == 0:
        raise KeyError('No keys entered')
    else:
        if file_format == 'csv':
            Csv.write_csv(key_list)
        elif file_format == 'json':
            Json.write_json(key_list)
        else:
            raise ValueError('Expected only csv or json as file formats.')  # raise an error if the format does not exist
