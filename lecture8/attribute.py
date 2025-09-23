# class Student:
#         college_name = "ABC colage"

#         def __init__(self, name,marks):
#             self.name = name
#             self.marks= marks
#         # print(self)
#         print("creating a new student inn databse..")

# s1 = Student("Karna",98)
# print(s1.name,s1.marks)

# s2 = Student("Arjun",89)
# print(s2.name,s2.marks)


class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome student,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Karan", 97)
s1.welcome()
print(s1.get_marks())
s2 = Student("Arjun", 89)
s2.welcome()
print(s2.get_marks())
