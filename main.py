import sys
from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = get_num_chars(text)
    sorted_list = get_sorted_list(num_chars)
    for char_dict in sorted_list:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

main()