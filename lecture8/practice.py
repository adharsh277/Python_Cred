class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks

    def get_avg(self):
        sum= 0
        for val in self.marks:
            sum+= val
        # return sum/len(self.marks)    
        print("hi", self.name, "Your avg score is :",sum/3)

s1= Student("Tony", [99,96,95])
s1.get_avg()

s1.name="Chris evans"
s1.get_avg()