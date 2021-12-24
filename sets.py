# sets data structure
s = set()
print(type(s))
a = [1, 2, 3, 4, 5]
s_creation = set(a)
print(s_creation)
s.add(1)
s.add(2)
s.add(3)
print(s)

# sets operation

# union
A = {1, 2, 3, 4, 5, 6}
B = {3, 4, 5, 8}
unity = A.union(B)
print(unity)

# Intersection
A = {1, 2, 3, 4, 5, 6}
B = {3, 4, 5, 8}
intersect = A.intersection(B)
print(intersect)
