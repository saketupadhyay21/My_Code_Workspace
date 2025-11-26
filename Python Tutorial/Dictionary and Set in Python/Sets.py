#Sets cannot store list and dictionaries
#Sets elements are immutable but you can still add or remove elements in a set

collections = {1, 2, 3, 4}

print(type(collections))

types = set()
print(type(types)) #empty set syntax

types.add(1)
types.add("Saket")
types.add(85.2)

print(types)