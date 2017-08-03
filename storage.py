""" contains implementation of local caching """


# core modules
import os
import pickle


STORAGE_DIR = os.path.join(os.getcwd(), "data")

FILE_EXIST_ERR = "file already exists"

FILE_NEXIST_ERR = "file does not exist"


def check(filename):
    """ check if provided filename exists in the default directory
    Args:
        filename: string
    Returns:
        boolean
    """
    return os.path.exists(os.path.join(STORAGE_DIR, filename))


def save(pyobj, filename):
    """ serialise a python object and save it at default directory
    Args:
        pyobj: any
        filename: string
    Returns:
        None
    Raises:
        FileExistError - if file exists to prevent overwrite
    """
    if check(filename):
        raise FileExistsError(FILE_EXIST_ERR)
    with open(os.path.join(STORAGE_DIR, filename), "wb") as outfile:
        pickle.dump(pyobj, outfile)


def load(filename):
    """ deserialise a python object from default directory
    Args:
        filename: string
    Returns:
        any
    Raises:
        FileNotFoundError - when filename cannot be found on STORAGE_DIR
    """
    if not check(filename):
        raise FileNotFoundError(FILE_NEXIST_ERR)
    with open(os.path.join(STORAGE_DIR, filename), "rb") as infile:
        pyobj = pickle.load(infile)
    return pyobj
