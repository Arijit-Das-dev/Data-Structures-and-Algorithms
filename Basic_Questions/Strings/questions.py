# Reverse a string.
# Check whether a string is a palindrome.
# Count vowels and consonants.
# Remove all digits from a string.
# Remove all special characters.
# Convert a sentence into title case.
# Count the frequency of each character.
# Find the longest word in a sentence.
# Replace multiple spaces with a single space.
# Count how many times a word appears.


# Reverse a string.
# method 1
string1 = "arijit"
print(string1[::-1])

# method 2
string2 = "arijit"
newstring = ""    

for i in range(len(string2)-1, -1, -1):
    newstring += string2[i]
print(newstring)