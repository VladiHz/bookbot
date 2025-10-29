import sys
from stats import get_num_words
from stats import count_character_repetition
from stats import format_report

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookpath = sys.argv[1]
    #bookpath = 'books/frankenstein.txt'
    num_words = get_num_words(bookpath)
    #print(f"Found {num_words} total words")
    char_repetition = count_character_repetition(bookpath)
    #print(char_repetition)
    report = format_report(bookpath, num_words, char_repetition)
    print(report)