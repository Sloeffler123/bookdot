def words_in_book(file_path):
    with open(file_path) as file:
        file_content = file.read().split()
        num_words = len(file_content)    
    print(f'{num_words} words found in the document')

def letters_in_book(file_path):
    with open(file_path) as file:
        file_content = file.read().lower()
        
        letters = {}
        for i in file_content:
            if i not in letters and i.isalpha() == True:
                occurances = file_content.count(i)
                letters.update({i : occurances,})
        return letters



def organized_dict(file_path): 
    sorted_dict_letters = dict(sorted(letters_in_book('books/frankenstein.txt').items(), key=lambda x:x[1], reverse=True))
    
    for k,v in sorted_dict_letters.items():
        print(f'{k}: {v}')
    
