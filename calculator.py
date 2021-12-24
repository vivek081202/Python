# python program for calculator

print("Enter an Arithmetic Operator: ")
op = str(input())

print("Enter 1st number: ")
number1 = int(input())

print("Enter 2nd number: ")
number2 = int(input())

if op == '+':
    result = number1 + number2
    print("Your sum is: ", result)

elif op == '*':
    result = number1 * number2
    print("Multiplication of two numbers: ", result)

elif op == '-':
    result = number1 - number2
    print("Subtraction of two numbers: ",result)

elif op == '/':
    result = number1 / number2
    print("Remainder : ", result)

elif op == '%':
    result = number1 % number2
    print("Remainder : ", result)
else:
    print("Wrong operator inserted")