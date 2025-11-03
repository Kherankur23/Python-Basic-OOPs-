#write a python program to create a class that stores the name and marks of 3 subject of a student
#take the input from the user and display the name and the marks of the subject
#make a funtion that returns the average of the marks entered by the user 


'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def average(self):
        avg=sum(marks)/len(marks)
        print("THE NAME OF THE STUDENT :",self.name)
        print("AVERAGE SCORE OF THE SUBJECT ARE :",avg)

marks=[]
n=int(input("ENTER THE NUMBER OF SUBJECTS :"))
for i in range(0,n):
    x=int(input("ENTER THE MARKS OF SUBJECT :"))
    marks.append(x)
name=input("ENTER THE NAME OF THE STUDENT :")
s1=Student(name,marks)
s1.average()'''


#Create a Account class with 2 attributes - balance and account no
#create methods for debit,credit and printing the balance
#Create a banking system 

'''class Account: 

    #constructor 
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
    
    #debit method :

    def debit_money(self):
        print("-----------------------------DEBIT-----------------------------------------")
        x=int(input("ENTER THE AMOUNT YOU WANT TO DEBIT :"))
        if x>self.bal:
            print("NOT SUFFICIENT BALANCE IN YOUR ACC....")
        else:
            self.bal=self.bal-x
            print("MONEY DEBITED FROM YOUR ACCOUNT...")
        
    
    #credit method :

    def credit_money(self):
        print("----------------------------CREDIT------------------------------------------")
        y=int(input("ENTER THE AMOUT YOU WANT TO CREDIT :"))
        self.bal=self.bal+y
        print("AMOUNT IS CREDITED IN YOUR ACC...")
    

    #Displaying the Balance ammout :

    def display_bal(self):
        print("<--------------------------DISPLAY----------------------->")
        print("ACCOUNT NO :",self.acc)
        print("BALANCE AMOUT:",self.bal)
        print("----------------------------------------------------------------------")
    

bal=int(input("ENTER THE ACC BALANCE :"))
acc=int(input("ENTER THE ACCOUNT NO :"))
acc1=Account(bal,acc)
acc1.debit_money()
acc1.credit_money()
acc1.display_bal()'''




#Define a Circle class to create a cirlce with radius r using the constructor
#define an Area() method of the class which calculates the area of the circle
#define an Perimeter() method of the class which allows us to calculate the perimeter of the circle


'''class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.13*self.radius**2
    
    def perimeter(self):
        return 2*3.14*self.radius


x=int(input("ENTER THE RADIUS OF THE CIRCLE:"))
c1=Circle(x)
print(c1.area())
print(c1.perimeter())'''


#Define a class Employee with attribute role,department,salary.
#This class should also contain show_Detail() method
#Also create a class Enginner which inherits the properties of the base class{Employee} and display the name and age.
'''
class Employee:

    def __init__(self,role,dpt,salary):
        self.role=role
        self.dpt=dpt
        self.salary=salary

    def Show_details(self):
        print("EMPLOYEE ROLE IS :",self.role)
        print("EMPLOYEE DEPARTMENT IS :",self.dpt)
        print("EMPLOYEE SALARY IS :",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("NAME OF THE EMPLOYEE:",self.name)
        print("AGE OF THE EMPLOYEE:",self.age)
        super().__init__("ENGINEER","IT","$250000")

en1=Engineer("SAM","40")
en1.Show_details()
'''

#create a class Order which stores the items no , item name and its price 
#use Dunder Funtion __gt__() to convey that :
#order 1 > order 2 if price of order1>price of order 2:

'''
class Order:
    def __init__(self,item_no,item_name,item_price):
        self.item_no=item_no
        self.item_name=item_name
        self.item_price=item_price

    def show_details(self):
        print("ITEM NO:",self.item_no)
        print("ITEM NAME:",self.item_name)
        print("ITEM PRICE :",self.item_price)

    def __gt__(self,o2):   #Dunder funtion used to check if the value o2 is greater or not 
        return self.item_price>o2.item_price

o1=Order("1","tea",20)
o2=Order("2","coffee",25)
o1.show_details()
o2.show_details()
print("IS ORDER 2 GREATER THAN ORDER 1:",o2>o1)
'''






