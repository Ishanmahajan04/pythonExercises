import string

file_name = input('Enter the file name (ex. palindromes.txt)> ')
unwanted = string.punctuation + ' '

def is_palindrome(str):
  # Remove the unwanted chars
  new_str = filter(lambda x: x not in unwanted, str.lower())
  if new_str == new_str[::-1]:
    return True

with open(file_name, 'r') as f:
  for line in f:
    # Here I used rstrip to remove the newline (\n) at the end of the line
    if is_palindrome(line.rstrip()):
      print (line.rstrip())