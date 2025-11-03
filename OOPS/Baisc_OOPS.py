#THIS INCLUDES ALL THE BASIC OF CLASS AND OBEJCTS AND CERTAIN INFO ABOUT METHODS AND STATIC METHOD

class Student:   #Student is the class 
    
    college_name="XYZ UNIVERSITY"  # college_name is a class attribute as its same for all the Students
    def __init__(self):    #Default constructor in python.
        pass      #pass statement does nothing when executed and is used to avoid syntax errors in situations where a statement is syntactically required but no action is needed.
    
    def __init__(self,fullname,marks):    #Parameterized constructor in python.
        self.name=fullname #self.name is a instance/Object attribute
        self.marks=marks   #self.marks is also a instance/Object attribute
        print("Student data added into the database...")
    
    @staticmethod     #decorater and this converts the below funtion into static function
    def Welcome():    #here Welcome(self) is a method created on the object
        print("WELCOME Student :",s1.name)

s1=Student("KARAN",78)   #s1 is the object of Student class
s1.Welcome()
print("NAME OF THE STUDENT :",s1.name)
print("COLLEGE :",s1.college_name)
print("MARKS SCORED :",s1.marks)


s2=Student("ROHAN",90)    #s1,s2 : The variables that store the data are called as "ATTRIBUTES"
s2.Welcome()
print("NAME OF THE STUDENT :",s2.name)
print("COLLEGE :",s2.college_name)
print("MARKS SCORED :",s2.marks) 


