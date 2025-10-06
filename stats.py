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