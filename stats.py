# turns text file to string
def get_book_text(path):
    with open(path) as s:
        return s.read()
# Prints number of words in a document
def word_count(path):
    superlist = get_book_text(path)
    return len(superlist.split())
def character_count(path):
    superlist = get_book_text(path)
    output_dictionary = {"a":0}
    for c in superlist:
        character = c.lower()
        if character in output_dictionary:
            output_dictionary[character] += 1
        else:
            output_dictionary[character] = 1
    return output_dictionary
