# Expected output
"""
* * * * 
* * * 
* *
*

row (i) -> 4
column (j) -> 4
"""
for i in range(1, 10):
    for j in range(i, 10):
        print("*", end=" ")
    print()