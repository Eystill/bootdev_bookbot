def get_book_text_count():
    text_list = []
    text = ""
    with open ('books/frankenstein.txt') as file:
        text = file.read()
    text_list = text.split()
    count_of_words = len(text_list)
    return(count_of_words)