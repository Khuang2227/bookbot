def get_book_text():
    with open("books/frankenstein.txt") as file:
        text = file.read()
        return text

def main():
    return get_book_text()