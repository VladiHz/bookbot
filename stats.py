def get_book_text(book_path):
    with open(book_path, 'r') as file:
        return file.read()
    
def get_num_words(book_path):
    wholetext = get_book_text(book_path)
    words = wholetext.split()
    return len(words)

def count_character_repetition(book_path):
    letras = {}
    wholetext = get_book_text(book_path)
    for char in wholetext:
        if char.lower() in letras:
            letras[char.lower()] += 1
        else:
            letras[char.lower()] = 1
    return letras