import os
import time

FOLDER_PATH = r"F:\Downloads\miyoo\tiny-best-set-go\Roms\FC"
FILE_EXTENSION = ".zip"


def remove_parentheses(file_name, bracket_type="()"):

    new_file_name = file_name
    while True:
        open_par = new_file_name.find(bracket_type[0])
        close_par = new_file_name.find(bracket_type[-1]) + 1
        if open_par and close_par:
            new_file_name = new_file_name.replace(new_file_name[open_par:close_par], "")
        else:
            break

    return new_file_name


def remove_trailing_spaces(file_name):
    base_name, file_extension = os.path.splitext(file_name)
    base_name = base_name.rstrip()
    new_file_name = base_name + file_extension
    return new_file_name


def rename_files(directory_path, extension=None):
    files = os.listdir(directory_path)

    for file_name in files:
        old_file_path = os.path.join(directory_path, file_name)

        if os.path.isfile(old_file_path) and extension in old_file_path:
            new_file_name = remove_parentheses(file_name, bracket_type="()")  # REMOVE PARENTHESES GOES HERE
            new_file_name = remove_parentheses(new_file_name, bracket_type="[]")  # REMOVE PARENTHESES GOES HERE
            new_file_name = remove_trailing_spaces(new_file_name)

            new_file_path = os.path.join(directory_path, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {file_name} to {new_file_name}')
            time.sleep(0.11)


if __name__ == '__main__':
    rename_files(FOLDER_PATH, extension=FILE_EXTENSION)
