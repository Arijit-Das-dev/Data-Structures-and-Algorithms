# Expected output
"""
3 
3 4
3 4 5
3 4 5 6
"""

for i in range(1, 5):
    for j in range(3, i+3):
        print(j, end=" ")
    print()