#Exercise 38, python 2

from string import punctuation

def average_word_length(file_name):
	with open(file_name, 'r') as f:
		for line in f:
			line = filter(lambda x: x not in punctuation, line)
			words = map(len, line.split())
	print (sum(words) / len(words))

average_word_length('sample.txt')