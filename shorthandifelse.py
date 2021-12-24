a = int(input("Enter a: "))
b = int(input("Enter B: "))

if a > b: print("A is greater than B")
print("B is greater than A") if a < b else print("A is grater than B")

a, b = b, a
print(a, b)
