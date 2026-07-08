# Check whether a string is a palindrome.


def check_pallindrome_string(string: str) -> bool:

    newString = ""
    for i in range(len(string)-1, -1, -1):
        newString += string[i]

    if string == newString:
        return True
    else:
        return False

string1 = "ABBA"
string2 = "ABCA"

print(check_pallindrome_string(string=string1))
print(check_pallindrome_string(string=string2))