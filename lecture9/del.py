# class Student:
#     def __init__(self,name):
#         self.name=name

# s1= Student("Shardad")
# print(s1.name)
# del s1
# print(s1)

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self,new_pass):
        print(self.__acc_pass)


acc1 = Account("12345","abcde")

print(acc1.acc_no)
# print(acc1.acc_pass)
print(acc1.reset_pass)




### cllassss

class Person:
    __name__="Unknown"

    def __hello(self):
        print("hello boboboi")

    def welcome(self):
        self.__hello()

p1=Person()

print(p1.welcome())
