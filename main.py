from stats import *
import sys

sys.argv

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", get_book_text_count(), "total words")
    print("--------- Character Count -------")
    sorted_chars = sorting(character_count())
    for item in sorted_chars:
        # Set a local variable to contain the "character" and "count" valies of the dictionary items in the list.
        character = item["character"]
        count = item["count"]
        print(f"{character}: {count}")
    print("============= END ===============")

main()