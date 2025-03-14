def get_book_text_count():
    text_list = []
    text = ""

    # While the file specified is open set the text variable to contain everything frmo the file
    with open ('books/frankenstein.txt') as file:
        text = file.read()          

    # split all the words of the text variable into a list of strings and set a list to contain all those strings
    text_list = text.split()
    count_of_words = len(text_list)
    return(count_of_words)

def character_count():
    character_values = {}
    letter_counter = 0
    text_string = ""

    # While the file specified is open set the text_string variable to contain everything frmo the file
    with open ('books/frankenstein.txt') as file:
        text_string = file.read()

        # loop through all characters in the text. .lower() forces lowercase characters
        for letter in text_string.lower():
            if letter == "a":
                letter_counter += 1
        
        # Add the value and key to the dictionary and reset the letter_counter
        character_values["a"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "b":
                letter_counter += 1
        
        character_values["b"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "c":
                letter_counter += 1
        
        character_values["c"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "d":
                letter_counter += 1
        
        character_values["d"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "e":
                letter_counter += 1
        
        character_values["e"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "f":
                letter_counter += 1
        
        character_values["f"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "g":
                letter_counter += 1
        
        character_values["g"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "h":
                letter_counter += 1
        
        character_values["h"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "i":
                letter_counter += 1
        
        character_values["i"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "j":
                letter_counter += 1
        
        character_values["j"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "k":
                letter_counter += 1
        
        character_values["k"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "l":
                letter_counter += 1
        
        character_values["l"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "m":
                letter_counter += 1
        
        character_values["m"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "n":
                letter_counter += 1
        
        character_values["n"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "o":
                letter_counter += 1
        
        character_values["o"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "p":
                letter_counter += 1
        
        character_values["p"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "q":
                letter_counter += 1
        
        character_values["q"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "r":
                letter_counter += 1
        
        character_values["r"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "s":
                letter_counter += 1
        
        character_values["s"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "t":
                letter_counter += 1
        
        character_values["t"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "u":
                letter_counter += 1
        
        character_values["u"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "r":
                letter_counter += 1
        
        character_values["v"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "v":
                letter_counter += 1
        
        character_values["w"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "w":
                letter_counter += 1
        
        character_values["x"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "x":
                letter_counter += 1
        
        character_values["x"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "y":
                letter_counter += 1
        
        character_values["y"] = letter_counter
        letter_counter = 0

        for letter in text_string.lower():
            if letter == "z":
                letter_counter += 1
        
        character_values["z"] = letter_counter
    
    return(character_values)