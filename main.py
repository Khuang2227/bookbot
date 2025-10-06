from stats import count_words, count_characters

def get_book_text(file_path):
    with open(file_path) as file:
        text = file.read()
        return text
    
def main():
    path = "books/frankenstein.txt"
    num_words = count_words(get_book_text(path))
    print(f"Found {num_words} total words.")
    print(count_characters(get_book_text(path)))

main()