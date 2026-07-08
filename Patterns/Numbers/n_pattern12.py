# Expected output
"""
3 4 5 6
3 4 5
3 4
3
"""

for i in range(1, 5):
    for j in range(3, 8-i):
        print(j, end=" ")
    print()