import os


# This function checks takes in a 'path' argument and checks if the filepath in that path exists or not
def does_file_exist(path):
    if not os.path.exists(path):
        raise Exception('Path is invalid')  # raise an exception if the filepath does not exist
    return True
