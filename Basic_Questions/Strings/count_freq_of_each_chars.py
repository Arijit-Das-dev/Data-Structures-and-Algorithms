# Count the frequency of each character.

chars = "aabbccddee"
freq = {}

for i in range(0, len(chars)):
    if chars[i] not in freq:
        freq[chars[i]] = 1
    else:
        freq[chars[i]] += 1

for char, count in freq.items():
    print(f"{char} : {count}")