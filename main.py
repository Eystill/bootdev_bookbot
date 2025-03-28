from stats import *
import sys

def main():
    try:
        # Path of file read from sys.argv position 1 and used in functions.
        book = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print("Found", get_book_text_count(book), "total words")
        print("--------- Character Count -------")
        sorted_chars = sorting(character_count(book))
        for item in sorted_chars:
            # Set a local variable to contain the "character" and "count" valies of the dictionary items in the list.
            character = item["character"]
            count = item["count"]
            print(f"{character}: {count}")
        print("============= END ===============")
    except:
        # If no book is specified by user, print guide and exit
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()