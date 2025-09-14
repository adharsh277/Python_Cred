student = {
    "name" : "rahul kumar",
    "subjects": {
        "phy" :97,
        "chem" :98,
        "math" :95,
    }
}

print(student)
print(student["subjects"]["chem"])
print(student.keys())
print(len(list(student.keys())))
print(len(student))