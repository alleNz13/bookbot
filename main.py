from stats import get_word_number
from stats import get_char_number


def get_book_text (filepath):

    with open(filepath) as f:
        file_content = f.read()
    return file_content
def main():
    filepath = "books/frankenstein.txt"
    content = get_book_text(filepath).split()
    strings = get_book_text(filepath).lower()
    word_num = get_word_number(content)
    char_nums = get_char_number(strings)
    

    #report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")




main()

