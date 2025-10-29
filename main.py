def get_book_text(book_path):
    with open(book_path, 'r') as file:
        return file.read()
    
if __name__ == "__main__":
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)