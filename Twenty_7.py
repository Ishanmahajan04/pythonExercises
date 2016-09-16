def words_length_one(words):
    wordsLength = []
    for word in words:
        wordsLength.append(len(word))
    return wordsLength

#
def words_length_two(words):
    return map(len, words)

def words_length_three(words):
    return [len(word) for word in words]

print (words_length_one(['lol', 'this', 'is', 'funny']))
print (words_length_two(['lol', 'this', 'is', 'NOT', 'funny']))
print(words_length_three(['or', 'is', 'it', '?']))