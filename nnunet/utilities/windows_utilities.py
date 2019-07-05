import os

def split_path(path):
    '''
    Splits a path into a list of directory strings, using the sorrect separator 
    for the currentlz used os. 
    The path may start with a slash.
    '''
    path = os.path.normpath(path)
    split_path = path.split(os.sep)
    split_path = list(filter(None, split_path))
    return split_path