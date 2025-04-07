def get_num_words(text):
  return len(text.split())

def sort_on(dict):
  return dict["count"]

def get_char_count(text):
  char_counts = {}
  text = text.lower()
  for c in text:
    
    if c in char_counts.keys():
      char_counts[c] +=1
    else:
      char_counts[c] = 1
  
  return char_counts

def get_char_list(char_counts):
  char_list = []

  for char in char_counts.keys():
    char_list.append({"char": char , "count": char_counts[char]})
  
  char_list.sort(key=sort_on, reverse=True)
  return char_list
