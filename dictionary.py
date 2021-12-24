# dictionary
d1 = {}
print(type(d1))

# Declaring & defining a dictionary
# vivek is key here and manager is value
d2 = {"Vivek": "Manager", "Mohit": "Accountant", "Prince": "Engineer",
      "Shubham": {"Microsoft": "Engineer", "online": "Freelancer"}}
print(d2["Prince"])
print(d2["Shubham"]["online"])

# Adding elements in dictionary
d2["Yogesh"] = "Supervisor"
print(d2)

# Deletion of elements from dictionary
del d2["Yogesh"]
print(d2)

# functions in dictionary

# using .cpy() function to copy dictionary
"""
using of pointers will create trouble in copying different elements from another dictionary
For instance
d2 is dictionary
if we do this, d3 = d2
del d3["name"]
it will also remove from d2 also therefore we will use .copy() function with dictionary to copy data of another 
dictionary
"""
d3 = d2.copy()
del d3["Prince"]
print(d2)
print(d3)

# .get() function
print(d2.get("Vivek"))

# .update() function
d2.update({"Leena": "CEO"})
print(d2)

# printing key values of dictionary d2
print(d2.keys())

# printing values of dictionary d2
print(d2.values())
print(d2.items())
