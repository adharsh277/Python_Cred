class Student:
    # name= "karna"



    #parameterixed  constructor
    def __init__(self, name,marks):
        self.name = name
        self.marks= marks
        # print(self)
        print("creating a new student inn databse..")

s1 = Student("Karna",98)
print(s1.name,s1.marks)

s2 = Student("Arjun",89)
print(s2.name,s2.marks)