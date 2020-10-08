from src.data import languages


class FetchData:
    @staticmethod
    def get_from_data_file(list_of_keys):
        # I created a list which would store the information retrieved from data.py based on keys provided
        list_all = []

        for key in list_of_keys:
            if key in languages.keys():
                list_all.append(languages[key])
            else:
                raise KeyError('This key does not exist.')  # raise a keyError exception if key does not exist
        return list_all
