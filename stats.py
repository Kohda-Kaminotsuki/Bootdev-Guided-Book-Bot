# turns text file to string
def get_book_text(filepath):
    with open(filepath) as s:
        return s.read()
# Prints number of words in a document
def word_count():
    superlist = get_book_text("books/frankenstein.txt")
    return len(superlist.split())
def character_count():
    superlist = get_book_text("books/frankenstein.txt")
    output_dictionary = {"a":0}
    for c in superlist:
        character = c.lower()
        if character in output_dictionary:
            output_dictionary[character] += 1
        else:
            output_dictionary[character] = 1
    return output_dictionary
