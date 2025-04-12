# Prints number of words in a document
def word_count():
    superlist = get_book_text("books/frankenstein.txt")
    return len(superlist.split())
