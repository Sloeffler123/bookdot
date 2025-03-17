def words_in_book(file_path):
    with open(file_path) as file:
        file_content = file.read().split()
        num_words = len(file_content)    
    return num_words
    
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
    sorted_dict_letters = dict(sorted(letters_in_book(file_path).items(), key=lambda x:x[1], reverse=True))
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}')
    print('----------- Word Count ----------')
    print(f'Found {words_in_book(file_path)} total words')
    print('--------- Character Count -------')
    for k,v in sorted_dict_letters.items():
        print(f'{k}: {v}')
    print('============= END ===============')
