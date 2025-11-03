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




#



    

