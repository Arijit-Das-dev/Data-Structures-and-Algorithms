# Expected output
"""
* * * * 
* * * 
* *
*

row (i) -> 4
column (j) -> 4
"""

# method 1
for i in range(1, 5):
    for j in range(i, 5):
        print("*", end=" ")
    print()


# method 2
for i in range(1, 5):
    for j in range(1, 6-i):
        print("*", end=" ")
    print()