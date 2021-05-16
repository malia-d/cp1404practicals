import shutil
import os


def main():
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
