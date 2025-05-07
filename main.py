def main():
    print("greetings boots")
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     character_dict = get_character_count(text)
#     char_count_dict = get_list_of_chars(character_dict)
#     print(f"--- Book Report ---")
#     print(f"There were {num_words} found in this book")
#     print()

#     for char_count in char_count_dict:
#         print(f"There are {char_count["count"]} of the letter {char_count["char"]} in this book.")
#     print("--- End of Report ---")


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()

# def get_character_count(text):
#     lower_text = text.lower()
#     char_dict = {}
#     for letter in lower_text:
#         if letter not in char_dict:
#             char_dict[letter] = 1
#         else:
#             char_dict[letter] += 1
#     return char_dict

# def sort_on(di):
#     return di["count"]

# def get_list_of_chars(dictionary):
#     char_count_list = []
#     for char in dictionary:
#         if char.isalpha():
#             char_count_list.append({"char": char, "count": dictionary[char] })
#     char_count_list.sort(reverse=True, key=sort_on)
#     return char_count_list

main()
