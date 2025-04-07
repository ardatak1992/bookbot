from stats import get_num_words, get_char_count, get_char_list
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    filecontets = f.read()
    return filecontets

def print_report(filepath):

  frankenstein_book = get_book_text(filepath)
  num_words = get_num_words(frankenstein_book)
  char_list = get_char_list(get_char_count(frankenstein_book))

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for char_dict in char_list:
    if char_dict["char"].isalpha():
      print(f"{char_dict["char"]}: {char_dict["count"]}")
  print("============= END ===============")

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  print_report(sys.argv[1])

main()
