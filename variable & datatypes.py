# Data types & Variables
print("Hello user this is file for Data types & Variables")
var1 = "Vivek"
var2 = 4
var3 = 67
var4 = " Singh"
print(var3 + var2)
print(var1 + var4)
print(type(var1))
print(type(var2))
print(type(var3))

# Type Casting
print(str(var2) + str(var3))
"""
Functions used in type casting
str() to convert into string values
float() to convert into float values
int() to convert into integer values
"""

# High level type casting
print(5 * int(str(var2) + str(var3)))

# print statement multiple times
print(5 * "Vivek is a good boy\n")
# input from user

print("Enter 1st number")
number = int(input())

print("Enter 2nd number")
number1 = input()

result = int(number) + int(number1)
print("your sum is", int(result))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
