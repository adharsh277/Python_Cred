class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, other):
        newReal = self.real + other.real
        newImg = self.img + other.img
        return Complex(newReal, newImg)

num1 = Complex(2, 3)
num1.showNumber()

