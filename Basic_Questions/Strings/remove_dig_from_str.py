# Remove all digits from a string.
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