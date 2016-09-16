
import string
file_name = raw_input('Enter file name (ex. semordnilaps.txt)> ')
unwanted = string.punctuation + ' '

def clean(str):
  cleaned_str = filter(lambda x: x not in unwanted, str.rstrip().lower())
  return cleaned_str

found = []
with open(file_name, 'r') as f:
  for line in f:
    if clean(line)[::-1] in found:
      print clean(line), clean(line)[::-1]
    else:
      found.append(clean(line))