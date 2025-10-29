from stats import get_num_words
from stats import count_character_repetition
    
if __name__ == "__main__":
    bookpath = 'books/frankenstein.txt'
    num_words = get_num_words(bookpath)
    print(f"Found {num_words} total words")
    char_repetition = count_character_repetition(bookpath)
    print(char_repetition)