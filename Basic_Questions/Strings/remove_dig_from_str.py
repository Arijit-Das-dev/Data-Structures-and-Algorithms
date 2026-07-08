# Remove all digits from a string.

# method 1
string = "abcdefghijklmnopqrstuvwxyz12345678910"

new_arr = []
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for char in string:
    if char not in nums:
        new_arr.append(char)
    else:
        continue

strings = "".join(new_arr)
print(strings)

# method 2
characters = "abcdefghijklmnopqrstuvwxyz12345678910"
new_chars = ""

for char in characters:
    if not char.isdigit():
        new_chars += char

print(new_chars)