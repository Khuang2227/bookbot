def get_book_text(file_path):
    with open(file_path) as file:
        text = file.read()
        return text
    
def count_words(text):
    words = text.split()
    return len(words)

def main():
    path = "books/frankenstein.txt"
    num_words = count_words(get_book_text(path))
    print(f"Found {num_words} total words.")

main()