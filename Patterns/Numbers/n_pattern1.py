# Expected output
"""
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

row (i) -> 5
column (j) -> 4

"""
for i in range(1, 6):
    for j in range(1, 5):
        print(j, end=" ")
    print()