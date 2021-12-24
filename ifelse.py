# if else statements
var1 = int(6)
var2 = int(input())

if var2 > var1:
    print("Greater")
else:
    print("Smaller")

# searching in list using if else

A = [1, 2, 3, 5]
if 5 in A:
    print("Yes it is in A")
else:
    print("No it is not there")

# age program
print("Enter an age: ")
Age = int(input())
if Age >= 7 & Age <= 100:
    if Age > 18:
        print("Your are eligible to Drive a vehicle & to vote")
    elif Age < 18:
        print("You are not eligible for anything")
    elif Age == 18:
        print("You are eligible to most of the things")
    else:
        print("Wrong age inserted")
elif Age > 100 & Age < 7:
    print("Age exceeded ! wrong insertion")
