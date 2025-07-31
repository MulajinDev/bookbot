import sys
from stats import get_word_count, char_counts, sort_counts

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    bookpath = sys.argv[1]
    booktext = get_book_text(bookpath)
    words = get_word_count(booktext)
    counts = char_counts(booktext)
    sorted = sort_counts(counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in sorted:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()
