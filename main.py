from stats import *

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", get_book_text_count(), "total words")
    print("--------- Character Count -------")
    print(sorting(character_values))
    print("============= END ===============")

main()