def main():
  book_path = "books/frankenstein.txt"
  text = read_file(book_path)
  num_words = get_num_words(text)
  num_of_chars = get_num_of_characters(text)
  # print(f"{num_words} words found in the document")
  # print(f"Karakter Listesi: {num_of_chars}")
  print("--- Begin report of books/frankenstein.txt ---")
  create_report(dict_to_sorted_list(num_of_chars))
  print("--- End report ---")


def read_file(book_path):
  with open(book_path) as f:
    file_contents = f.read()
  return file_contents
  
def get_num_words(text):
  return len(text.split())

def get_num_of_characters(text):
  d = {}
  for i in text:
    i = i.lower()
    if i in d:
      d[i] += 1
    else:
      d[i] = 1 
  return d

def sort_on(d):
  return d["num"]

def dict_to_sorted_list(dic):
  sorted_list = []
  for i in dic:
    sorted_list.append({"char":i,"num":dic[i]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

def create_report(sorted_list):
  for item in sorted_list:
    if item["char"].isalpha():
      print(f"The '{item['char']}' character was found {item['num']} times")

main()