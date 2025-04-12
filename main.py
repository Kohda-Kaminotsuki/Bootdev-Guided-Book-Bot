from stats import word_count
from stats import character_count
# Prints the entire text of the document
def main():
    print(get_book_text("books/frankenstein.txt"))


# Debug Check
total_words = word_count()
#print(word_count())
#print(character_count())
character_count_list = character_count()
sorted_character_count = (dict(sorted(character_count_list.items(), key=lambda item: item[1], reverse=True)))




print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")
for c in sorted_character_count:
    if str.isalpha(c):
        print(f"{c}: {sorted_character_count[c]}")
    else:
        pass
print("============= END ===============")
