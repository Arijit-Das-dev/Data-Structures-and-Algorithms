# Check whether a string is a palindrome.


def check_Pallindrome_String(string: str) -> bool:

    newString = ""
    for i in range(len(string)-1, -1, -1):
        newString += string[i]

    if string == newString:
        return True
    else:
        return False

string1 = "ABBA"
string2 = "ABCA"

print(check_Pallindrome_String(string=string1))
print(check_Pallindrome_String(string=string2))