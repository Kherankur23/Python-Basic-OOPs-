#INHERITANCE METHODS:

#Single Inheritance#

'''class Car:    #THIS IS THE BASE CLASS OF THE PYTHON PROGRAM
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped...")
    
class ToyotaCar(Car):   #THIS IS THE DERIVED CLASS HAVING THE BASE CLASS AS Car
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("Prius")
print(Car.start())
print(Car.stop())'''


#Inheritance is of 3 types :
#(1) Single level inhertiance : Its a inheritance when there is only one derived class and one base class
#(2) Multiple inheritance : Its a inheritance when there is only one derived class but more than one base class
#(3) Multilevel inheritance : Its a inhertance when there a one base class through which a derived class is created and then
                             #this derived class is responsible to create another derived class forming a chain of inheritance


#Multilevel Inheritance

'''class Car:    #THIS IS THE BASE CLASS OF THE PYTHON PROGRAM
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped...")
    
class ToyotaCar(Car):   #THIS IS THE DERIVED CLASS HAVING THE BASE CLASS AS Car
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("Disel")
print(Car.start())
print(Car.stop())'''



#Multiple Inheritance#

'''class A:   #BASE CLASS 1
    varA="WELCOME TO CLASS A "
class B:  #BASE CLASS 2
    varB="welcome to class B"
class C(A,B):  #DERIVED CLASS HAVING BASE CLASS A AND CLASS B
    varC="Welcome to class C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)'''



#Super() Method :

class Car:  

    def __init__(self,type):
        self.type=type 
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped...")
    
class ToyotaCar(Car):   
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

car1=ToyotaCar("Fortuner","Eletric")
print(Car.start())
print(Car.stop())

