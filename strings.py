Quality = "vivek is a good boy"
Quality1 = "Videodisks"
print(Quality)
print(Quality[0:5])
print(Quality[0:5:2])
print(Quality[::-1])
# using length function len()
print(len(Quality))

# string built in functions
# .isalnum() is used to check spaces between words if space is there it will return (False) else (True).
print("\n")
print(Quality.isalnum())
print(Quality1.isalnum())
print("\n")
# .isalpha() is used to check spaces between words if space is there it will return (False) else (True)
print(Quality.isalpha())

""".endswith() is used to check boolean value if mentioned string inside function will be there in declared variable it 
will return return true else false"""
print(Quality1.endswith("disks"))

# .count() is used to count number of times character mentioned in function of string
print(Quality.count("o"))

# .capitalize is used to make word's first letter of string in uppercase  .
print(Quality.capitalize())

# .find is used to find the word index where it starts from in a string
print(Quality.find("is"))

# .lower is to make whole string in lowercase and .upper is vice-versa of .lower
print(Quality.lower())
print(Quality.upper())

# .replace is used to old into new word in a string
print(Quality.replace("good", "handsome"))
