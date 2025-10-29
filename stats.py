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

def sort_on(items):
    return items["num"]

def sort_dictionary_by_value(d):
    list_dict_char = []
    for item in d:
        list_dict_char.append({"char":item, "num":d[item]})
    #print(list_dict_char)
    list_dict_char.sort(key=sort_on, reverse=True)
    return list_dict_char


def format_report(bookpath, num_words, char_repetition):
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {bookpath}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {num_words} total words\n"
    report += "--------- Character Count -------\n"
    sorted_chars = sort_dictionary_by_value(char_repetition)
    for d in sorted_chars:
        if d["char"].isalpha():
            texto = str(d["char"])
            report += f"{texto}: {d["num"]}\n"
    report += "============= END ===============\n"
    return report