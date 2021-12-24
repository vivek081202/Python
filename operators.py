# operator in python
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators

print("Arithmetic operators")
print("\n")
print("5 + 32 = ", 5+32)
print("5 - 32 = ", 5-32)
print("5 * 32 = ", 5*32)
print("5 / 32 = ", 5/32)
print("5 % 32 = ", 5 % 32)
print("5 // 32 = ", 5 // 32)
print("5 ** 32 = ", 5 ** 3)

# Assignment operators
print("\n")
print("Assignment operators")
x = 5
print("After assigning some value to x: ", x)
x += 7
print("After assigning & incrementing value of x: ", x)
x %= 7
print("After assigning with mod value of x: ", x)

# comparison operators
print("\n")
print("comparison operators")
i = 10
print("You will get false bcz value of i is assigned as 10 we are comparing from 11: ", i == 11)

# logical operators
print("\n")
print("logical operators")
a = True
b = False
print(a and b)
print(a or b)
# print(a not b)

# Identity operators
print("\n")
print("Identity operators")
print(a is b)
print(a is not b)
print(4 is not 5)
print(4 is 4)

# Membership operators
print("\n")
print("Membership operators")
list1 = [3, 34, 32, 23, 23, 11]
print(23 in list1)
print(233 not in list1)

# Bitwise operators
print("\n")
print("Bitwise operators")
# 0 = 00
# 1 = 01
# 2 = 10
# 3 = 11
print(0 | 1)
print(0 | 3)
print(1 | 3)
print(0 & 2)
