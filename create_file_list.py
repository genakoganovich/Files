from os import listdir
from os.path import isfile, join

lines_file = 'full_list_of_lines.txt'
lines_file_plus_column = 'full_list_of_lines_plus_column.txt'
sgy_path = ''


def create_file_list(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def read_lines_to_list(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def add_column(path, file_name):
    file_list = create_file_list(path)
    line_list = read_lines_to_list(file_name)
    return []
