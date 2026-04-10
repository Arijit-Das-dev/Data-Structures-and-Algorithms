"""calculate occurrence of each integer number in an array"""

arr = [1, 1, 1, 2, 4, 2, 4, 5, 6, 5]

hashMap = {}

for i in arr:
    if i not in hashMap:
        hashMap[i] = 1
    else:
        hashMap[i] += 1

for x, y in hashMap.items():
    print(f"Number {x} occurred {y} times")