from stats import words_in_book, letters_in_book, organized_dict

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():
    print(get_book_text('books/frankenstein.txt')) 



words_in_book('books/frankenstein.txt')

letters = letters_in_book('books/frankenstein.txt')

print('============ BOOKBOT ============')
print(f'Analyzing book found at ')
print('----------- Word Count ----------')
    