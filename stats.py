def get_book_text(file_path: str):
    with open(file_path) as f:
        book_content = f.read()

    return book_content

def get_text_word_count(text: str):
    word_list = text.split()
    return len(word_list)

def get_character_count(text: str):
    lower_text = text.lower()
    count_dict = {}
    for ch in lower_text:
        if ch.isalpha():
            count_dict[ch] = count_dict.get(ch, 0) + 1
    
    return count_dict

def prepare_dict_list(character_count_dict: dict):
    list = []
    for k, v in character_count_dict.items():  
        if k.isalpha():
            dict = {
                "char": k,
                "num": v
            }
            list.append(dict)

    return list

def sort_on(dict: dict):
    return dict['num']

def get_processed_dict_list(character_count_dict: dict):
    prepared_list = prepare_dict_list(character_count_dict)
    prepared_list.sort(reverse=True, key=sort_on)
    return prepared_list

def print_report(file_path, word_count, processed_list):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for record in processed_list:
        print(f'{record['char']}: {record['num']}')
    print('============= END ===============')
