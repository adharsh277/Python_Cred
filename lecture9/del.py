class Student:
    def __init__(self,name):
        self.name=name

s1= Student("Shardad")
print(s1.name)
del s1
print(s1)