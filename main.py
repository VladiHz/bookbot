def get_book_text(book_path):
    with open(book_path, 'r') as file:
        return file.read()
    
if __name__ == "__main__":
    book_text = get_book_text('books/frankenstein.txt')
    words = book_text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")