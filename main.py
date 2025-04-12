def get_book_text(filepath):
    with open(filepath) as s:
        return s.read()

def main():
    print(get_book_text("books/frankenstein.txt"))

main()
