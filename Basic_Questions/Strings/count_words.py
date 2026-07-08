# Count how many times a word appears.

sentence = "I love India"

sentence = sentence.split()

freq = {}

for i in range(0, len(sentence)):
    if sentence[i] not in freq:
        freq[sentence[i]] = 1
    else:
        freq[sentence[i]] += 1

for word, count in freq.items():
    print(f"{word} : {count}")