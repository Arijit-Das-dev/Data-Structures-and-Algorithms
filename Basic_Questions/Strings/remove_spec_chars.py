# Remove all special characters.

characters = "#!@12av%$"
new_char = ""

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

for char in characters:
    if char not in special_chars:
        new_char += char

print(new_char)