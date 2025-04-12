# turns text file to string
def get_book_text(filepath):
    with open(filepath) as s:
        return s.read()
# Prints number of words in a document
def word_count():
    superlist = get_book_text("books/frankenstein.txt")
    return len(superlist.split())
