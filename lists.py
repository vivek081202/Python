# list creation which is mutable (we can modify elements in it)
Accessories = ["Mouse", "Keyboard", "Hard disks", "Computer Bag"]
print(Accessories)
print(Accessories[0], Accessories[2])

# list for numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(numbers[4], numbers[8])

# sorting in a list
numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

# string slicing
print(numbers[2:7:2])

# string functions
numbers.append(11)  # add elements at end of list
print(numbers)

numbers.insert(4, 71)  # used to insert an element anywhere in the string by index values
print(numbers)

numbers.remove(71)  # used to remove any element from the list
print(numbers)

numbers.pop()
print(numbers)  # used to remove last element from a list

numbers[9] = 11  # changing values of elements in a particular index
print(numbers)

# tuple creation which is immutable (we cannot modify elements in it)

tp = (1, 2, 3, 4)
print(tp)
# tp[3] = 5 we cant do this bcz tuple is immutable

# swapping of two numbers
"""
    1. Traditional method
    temp = A
    A = B
    B = temp
    
    2. python method
    A, B = B, A
"""
# python method for swapping of two numbers
A = 1
B = 2
A, B = B, A
print(A, B)


