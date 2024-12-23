def preLetterCase(input_string, letter):
    index = input_string.lower().find(letter.lower())
    if index == -1:
        return input_string.lower()
    before_letter = input_string[:index].lower()
    after_letter = input_string[index:].upper()
    return before_letter + after_letter
print(preLetterCase("CAtCHa", "a"))      
print(preLetterCase("Preteen", "e"))      
print(preLetterCase("You've got this", "m"))  
print(preLetterCase("Keep trying", "k"))  
