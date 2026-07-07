"""
Check whether a number is even or odd.
Find the largest among three numbers.
Calculate Simple Interest.
Calculate Compound Interest.
Find the quotient and remainder.
"""

# Check whether a number is even or odd.
num1 = int(input("Enter a number : "))

if num1 % 2 == 0:
    print(f"{num1} is Even")
else:
    print(f"{num1} is Odd")

# Find the largest among three numbers.
a = 10
b = 20
c = 30

if a>b and a>c:
    print(f"{a} is greater")
elif b>a and a>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")