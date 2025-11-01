class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


name=input("ENTER NAME:")
marks=int(input("ENTER MARKS:"))
s1=Student(name,marks)
print(s1.name,s1.marks)
del s1    #THIS WILL DELETE THE s1 ATTRIBUTE.


