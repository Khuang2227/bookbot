def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text_list = text.lower()
    char_count = {}
    for char in text_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_dict(text_dict):
    # Create an empty list to hold your dictionaries
    char_list = []
    
    # Loop through the dictionary
    for char in text_dict:
        # Get the count for this character
        count = text_dict[char]
        # Create a new dictionary with "char" and "num" keys
        char_dict = {"char": char, "num": count}
        # Add that dictionary to your list
        char_list.append(char_dict)
    
    # Sort the list using .sort()
    char_list.sort(reverse=True, key=sort_on)
    
    # Return the sorted list
    return char_list
    