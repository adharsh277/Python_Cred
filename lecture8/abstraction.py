
##Abstartction

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("car started..")

car = Car()
car.start()