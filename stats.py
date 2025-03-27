def get_book_text_count(book):
    text_list = []
    text = ""

    # While the file specified is open set the text variable to contain everything frmo the file
    with open (book) as file:
        text = file.read()          

    # split all the words of the text variable into a list of strings and set a list to contain all those strings
    text_list = text.split()
    count_of_words = len(text_list)
    return(count_of_words)

character_values = {}

def character_count(book):
    # While the file specified is open set the text_string variable to contain everything frmo the file
    with open (book) as file:
        text_string = file.read()

        # loop through all characters in the text. .lower() forces lowercase characters
        for letter in text_string.lower():
            # Only consider alphabetical characters
            if letter.isalpha():
                # Increment counter if letter already exists
                if letter in character_values:
                    character_values[letter] += 1
                # or create a new counter if it does not
                else:
                    character_values[letter] = 1
   
    return(character_values)

def sorting(character_count):
    sorted_list = []
    
    # Create a list of dictionaries with character and count
    for char, count in character_count.items():
        sorted_list.append({"character": char, "count": count})
    
    # Define a function to tell sort which key to use
    def sort_on(dict):
        return dict["count"]
    
    # Sort list from largest to smallest
    sorted_list.sort(reverse=True, key=sort_on)

    return(sorted_list)