# Expected output
"""
2 
2 3 
2 3 4
2 3 4 5
"""

for i in range(1, 5):
    for j in range(2, 2+i):
        print(j, end=" ")
    print()