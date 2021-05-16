"""
Create directories based on file extensions and move each file into their respective directory.

Sort Files 1. Created by Malia D'Mello, May 2021.
"""

import shutil
import os


def main():
    """Create directories and move files."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_extension = filename.split(".")[-1]
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        shutil.move(filename, file_extension)


main()
