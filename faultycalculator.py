# faulty calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4

print("Enter 1st num: ")
num1 = int(input())

print("Enter 2nd num: ")
num2 = int(input())

print("Enter operator: ")
op = input()

if num1 == 45 & num2 == 3 & op == "*":
    result = 555
    print(result)
elif num1 == 56 & num2 == 9 & op == "+":
    print("77")
elif num1 == 56 & num2 == 6 & op == '/':
    print("4")

elif op == '*':
    result = num1 * num2
    print(result)

elif op == '+':
    result = num1 + num2
    print(result)

elif op == '/':
    result = num1 / num2
    print(result)


