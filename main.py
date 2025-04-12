def get_book_text(filepath):
    with open(filepath) as s:
        return s.read()
# Prints the entire text of the document
def main():
    print(get_book_text("books/frankenstein.txt"))

# Prints number of words in a document
def word_count():
    superlist = get_book_text("books/frankenstein.txt")
    return len(superlist.split())

total_words = word_count()
print(f"{total_words} words found in the document")
