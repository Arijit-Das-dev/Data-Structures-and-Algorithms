# Count vowels and consonants.

chars = "aaeeiioouulmn"
vowels = ['a', 'e', 'i', 'o', 'u']

# method 1
vowels_count = 0
consonants_count = 0

for i in range(0, len(chars)):
    if chars[i] in vowels:
        vowels_count += 1
    else:
        consonants_count += 1


print(vowels_count)
print(consonants_count)


# method 2
vowels_count_1 = 0
consonants_count_2 = 0

for char in chars:
    if char in vowels:
        vowels_count_1 += 1
    else:
        consonants_count_2 += 1

print(vowels_count_1)
print(consonants_count_2)