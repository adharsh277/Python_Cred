student = {
    "name" : "rahul kumar" "kishore" "ramesh" "tipu",
    "subject" : {
        "phy" :97,
        "chem" :98,
        "math" :95,
    }
}

# print(student)
# print(student["subjects"]["chem"])
# print(student.keys())
# print(len(list(student.keys())))
# print(len(student))
# print(student.values())
# print(list(student.values()))

pairs = list(student.items())
print(pairs[1])

new_dict ={"name": "neha","age":13}
student.update(new_dict)
print(student)