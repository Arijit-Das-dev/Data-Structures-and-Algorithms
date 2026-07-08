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