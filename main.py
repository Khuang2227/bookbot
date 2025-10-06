from stats import count_words, count_characters, sort_dict, sort_on
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        text = file.read()
        return text
    
def main():
    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Use the second argument as the path to the book file
    path = sys.argv[1]
    text = get_book_text(path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # Word count section
    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    
    # Character count section
    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_chars = sort_dict(char_counts)
    
    # Only print alphabetic characters
    for char_data in sorted_chars:
        char = char_data["char"]
        count = char_data["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()