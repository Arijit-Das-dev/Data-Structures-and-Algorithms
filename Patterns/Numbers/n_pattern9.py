# Expected output
"""
2 3 4 5
2 3 4
2 3
2
"""

for i in range(1, 5):
    for j in range(2, 7-i):
        print(j, end=" ")
    print()