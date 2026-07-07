# Expected output
""" 
5 5 5 5 5
4 4 4 4
3 3 3 
2 2
1
"""

# method 1
num = 5
for i in range(1, 6):
    for j in range(1, 7-i):
        print(num, end=" ")
    num = num - 1
    print()

# method 2
num = 1
for i in range(5, 0, -1):
    for j in range(1, 7-num):
        print(i, end=" ")
    num = num + 1
    print()

# method 3
for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()