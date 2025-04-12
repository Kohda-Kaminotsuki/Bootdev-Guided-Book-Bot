import sys
input = sys.argv
if len(input) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_book = sys.argv[1]
from stats import word_count
from stats import character_count
# Prints the entire text of the document
def main():
    print(get_book_text(path_to_book))


# Debug Check
total_words = word_count(path_to_book)
#print(word_count())
#print(character_count())
character_count_list = character_count(path_to_book)
sorted_character_count = (dict(sorted(character_count_list.items(), key=lambda item: item[1], reverse=True)))




print("============ BOOKBOT ============")
print(f"Analyzing book found at {path_to_book}...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")
for c in sorted_character_count:
    if str.isalpha(c):
        print(f"{c}: {sorted_character_count[c]}")
    else:
        pass
print("============= END ===============")
