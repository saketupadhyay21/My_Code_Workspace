#Dictionaries are key value pairs, Keys can be string, integers, float, boolean etc.
#keys cannot be list and tuples
#keys cannot be duplicate
#dictionaries in python are immutable

info = {
    "key" : "Value",
    "name" : "Saket",
    "age" : 37,
    "marks" : [56, 67, 78],
    "percentage" : 84.2
}

#print(info)

#print(info["name"])

student = {
    "name" : "Saket",
    "subjects" : {
        "phy" : 78,
        "math" : 89,
        "Chem" : 87
    }
}

#print(student["subjects"]["phy"])
#print(student.keys())
#print(student.values())

#print(student.items())

student.update({"city" : "Delhi"})

print(student)