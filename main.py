def get_book_text(file_path):
    with open(file_path) as file:
        text = file.read()
        return text

def main():
    path = "books/frankenstein.txt"
    print(get_book_text(path))

main()