import os
import sys
import subprocess


def open_in_system(item):
    """
    Opens the supplied file system item in the default system manner.  The supplied item must be a full path to a file
    system item that has a default open method.
    :param item: A full path to a file system item that can be opened.
    :type item: str
    """
    if sys.platform == 'win32':
        os.startfile(item)
    else:
        opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
        subprocess.call([opener, item])


def create_directory(path):
    """
    Checks to see if the supplied directory path exists and creates the directory if it does not.  Also handles a
    FileExistsException which happens sometimes when multiple content items are being simultaneously downloaded and
    both threads try to create the same directory at the same time.
    :param path: The path of the directory that is checked and created.
    :type path: str
    :return: None if the path already exists
    """
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except FileExistsError:
            return None
    return None


def rename_directory_deleted(path):
    """
    Renames a folder with the '(deleted)' after the folder name.
    :param path: The path of the folder that is to be renamed with the "(deleted)" marker
    :return: True if the rename was successful and False if not.
    """
    try:
        print("Delete Path: %s" % path)
        if os.path.isdir(path):
            path = path[:-1] if path.endswith(os.sep) or path.endswith('/') else path
            os.rename(path, '%s (deleted)' % path)
        return True
    except PermissionError:
        return False

