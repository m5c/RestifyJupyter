"""
Author: Maximilian Schiedermeier
"""
import os
import shutil


def clear_cache(folder: str):
    """
    Function to clear all _contents_ of a folder specified by path.
    Taken from StackOverflow: https://stackoverflow.com/a/185941
    :return:
    """
    if not os.path.exists(folder):
        os.mkdir(folder)
        return

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
