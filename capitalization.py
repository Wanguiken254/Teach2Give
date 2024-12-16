input_string = input( "Enter any text")

def capitalize_words(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Capitalize the first letter of each word and join them back into a string
    capitalized_words = ' '.join(word.capitalize() for word in words)
    
    return capitalized_words
print(capitalize_words(input_string))