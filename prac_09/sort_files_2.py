import shutil
import os


def main():
    extension_to_folder = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_extension = filename.split(".")[-1]
        if file_extension not in extension_to_folder:
            category = input("What category would you like to sort {} files into? ".format(file_extension))
            extension_to_folder[file_extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        shutil.move(filename, extension_to_folder[file_extension])


main()
