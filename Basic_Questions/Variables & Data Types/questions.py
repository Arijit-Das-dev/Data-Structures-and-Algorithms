"""
1 Swap two variables without using a third variable.
2 Find the data type of different user inputs.
3 Convert a float to an integer and explain what happens.
4 Take a sentence and count the number of characters.
5 Find memory usage of different data types.
"""

# 1 Swap two variables without using a third variable.
a = 10
b = 20

a = a + b # 30
b = a - b # 10
a = a - b # 20
print(a, b)

# 2 Find the data type of different user inputs.
user1 = input("Enter a number : ")

user1 = int(user1)
print(type(user1))

# 3 Convert a float to an integer and explain what happens.
fl = 10.0
inti = int(fl)
print(inti)

# 4 Take a sentence and count the number of characters.
user_input = input("Enter some charecters : ")
count = 0
for char in user_input:
    count += 1
print(f"Number of charecter : {count}")

# 5 Find memory usage of different data types.
import sys

num = 10
pi = 3.14
name = "Arijit"
is_student = True
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {"name": "Arijit", "age": 21}

print(f"Integer : {sys.getsizeof(num)} bytes")
print(f"Float : {sys.getsizeof(pi)} bytes")
print(f"String : {sys.getsizeof(name)} bytes")
print(f"Bool : {sys.getsizeof(is_student)} bytes")
print(f"List : {sys.getsizeof(my_list)} bytes")
print(f"Tuple : {sys.getsizeof(my_tuple)} bytes")
print(f"Set : {sys.getsizeof(my_set)} bytes")
print(f"Dictionary : {sys.getsizeof(my_dict)} bytes")
