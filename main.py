from stats import get_book_text, get_text_word_count, get_character_count, get_processed_dict_list, print_report
import sys

def main():
    args = sys.argv

    if len(args) < 2:
        print('Usage: python3 main.py <path_to_book>')
        return sys.exit(1)
    file_path = args[1]

    book_text = get_book_text(file_path)
    word_count = get_text_word_count(book_text)
    character_count_dict = get_character_count(book_text)
    processed_list = get_processed_dict_list(character_count_dict)

    print_report(file_path, word_count, processed_list)

main()
