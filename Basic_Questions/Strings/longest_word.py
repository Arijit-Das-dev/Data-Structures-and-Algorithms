# Find the longest word in a sentence.

sentence = "i love India"

sentence = sentence.split()

longest_word = ""
print(len(longest_word))

for word in sentence:
    if len(word) > longest_word:
        longest_word = word
    
print(longest_word)