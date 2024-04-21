def open_and_read_file(file_path):
  """Opens and reads a file into a list.

  Args:
    file_path: The path to the file.

  Returns:
    A list of the lines in the file.
  """

  with open(file_path, "r") as f:
    lines = f.read().splitlines()
  return lines


def search_list(list_of_strings, joined_lines, starting_letter = ""):
  """Searches a list of strings for a given search term.

  Args:
    list_of_strings: A list of strings.
    search_term: The search term.

  Returns:
    A list of the strings in the list that contain the search term.
  """

  results = []
  search_term = set(joined_lines)
  for word in list_of_strings:
    if set(word).issubset(set(joined_lines)):
      if not starting_letter or word.startswith(starting_letter):
        if not double_letters(word):
          if len(word) > 3:
            results.append(word)
  return results

def restrict_words(line, possible_results):
  two_letter_options = []
  results = []
  for i in range(len(line)):
    for j in range(i + 1, len(line)):
      two_letter_options.append(line[i] + line[j])
      two_letter_options.append(line[j] + line[i])
	  
  for word in possible_results:
    if not any([x in word for x in two_letter_options]):
      results.append(word)	
  return results
  
def double_letters(word):
  for i in range (len(word)-1):
    if word[i] == word[i+1]:
      return True
  return False
  
def rank(possible_results, joined_lines):
  possible_results_with_ranking = []
  for word in possible_results:
    count = 0
    for letter in joined_lines:
      if letter in word:
        count += 1
    possible_results_with_ranking.append([word, count])
  return possible_results_with_ranking
  

# Example usage:

file_path = "./words.txt"
lines = open_and_read_file(file_path)
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
line4 = input("line 4: ")
starting_letter = input("starts with: ")

joined_lines = [*line1, *line2, *line3, *line4]
possible_results = search_list(lines, joined_lines, starting_letter)

possible_results = restrict_words(line1, possible_results)
possible_results = restrict_words(line2, possible_results)
possible_results = restrict_words(line3, possible_results)
possible_results = restrict_words(line4, possible_results)

possible_results_with_ranking = rank(possible_results, joined_lines)
possible_results_with_ranking.sort(key=lambda x: x[1])

for word in possible_results_with_ranking:
  print(word)