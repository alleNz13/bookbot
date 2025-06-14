from stats import get_word_number
from stats import get_char_number


def get_book_text (filepath):

    with open(filepath) as f:
        file_content = f.read()
    return file_content
def dictionary_split_sort(dict_ass):
    
    small_dicts = []
    for key, value in dict_ass.items():
        small_dicts.append({key: value})

    sortedlist = sorted(small_dicts, key=lambda item: list(item.values())[0],reverse=True)
   
    
    return sortedlist
        


def main():
    filepath = "books/frankenstein.txt"
    content = get_book_text(filepath).split()
    strings = get_book_text(filepath).lower()
    word_num = get_word_number(content)
    char_nums = get_char_number(strings)
    dict_list = dictionary_split_sort(char_nums)
    
    

    #report

     print("============ BOOKBOT ============")
     print(f"Analyzing book found at {filepath}...")
     print("----------- Word Count ----------")
     print(f"Found {word_num} total words")
     print("--------- Character Count -------")
     for character in dict_list:
        
         
            
     print("============= END ===============")




main()

