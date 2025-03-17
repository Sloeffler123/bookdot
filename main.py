from stats import words_in_book, letters_in_book, organized_dict
import sys

try:
    file_path = sys.argv[1]
except IndexError:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

organized_dict(file_path)
    