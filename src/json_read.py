import json


class JsonReader:
    """This class has a static method which is responsible for reading from the json file that was created."""
    @staticmethod
    def read():
        with open('data.json') as reader:
            return json.load(reader)
