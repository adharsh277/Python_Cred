class Car:
    colour= "red"
    @staticmethod
    def start():
        print("car started")
        
    @staticmethod
    def stop():
        print("car stoped")

class ToyotoCar(Car):
    def __init__(self,name):
        self.name= name

car1= ToyotoCar("Forctuner")
car2= ToyotoCar("prius")


print(car1.start())
# print(car1.name)
print(car1.colour)


## single inheritnce


       
class Car:
    @staticmethod
    def start():
        print("car started")
        
    @staticmethod
    def stop():
        print("car stoped")

class ToyotoCar(Car):
    def __init__(self,brand):
        self.brand= brand

class Fortuner(ToyotoCar):
    def __init__(self,type):
        self.type = type
       
car1 = Fortuner("diesel")
car1.start()


### multiple iheriteane

class A:
    varA = "welcome to class A"
class B:
    varB = " welcome to class B"
class C(A,B):
    varC = "welcome to class C"

c1= C()
print(c1.varC)
print(c1.varB)
print(c1.varA)