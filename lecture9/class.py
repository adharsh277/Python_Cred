class Person:
    name = "unknown"

    # def changeName(self, name):
    #     self.name =name
    @classmethod
    def changename(clas, name):
        clas.name = name

p1= Person()
p1.changename("rahul iswar")
print(p1.name)
print(Person.name)