#Function can be defined as a block of code which executes a specific task and only executes when its called
#function contains arguments which are defined inside parenthesis after naming the function

#lets take an example :
#write a funtion that performs arithematic operation on two numbers:
'''def add(a,b):  #function name - add(a,b) and it adds two values and (a,b) are the parameters of the function
    print(a+b)
def sub(a,b):  #function name - sub(a,b) and it substracts two values and (a,b) are the parameters of the function
    print(a-b)
def product(a,b):  #function name - multi(a,b) and it multiply two values and (a,b) are the parameters of the function
    print(a*b)
def dvd(a,b):  #function name - dvd(a,b) and it devides two values and (a,b) are the parameters of the function
    print(a/b)
num1=int(input("ENTER NUM1:"))
num2=int(input("ENTER NUM2:"))
add(num1,num2)   #num1,num2 are arguments for the funtion and function is called 
sub(num1,num2)   #num1,num2 are arguments for the funtion and function is called
product(num1,num2) #num1,num2 are arguments for the funtion and function is called 
dvd(num1,num2)   #num1,num2 are arguments for the funtion and funtion is called'''

#write a function to calculate the average marks of the student (take user input):

'''def average_of_marks():  #function name - average_of_marks and it calculates the average of the marks entered by the users
    avg=sum(x)/len(x)
    print("AVERAGE MARKS ARE :",avg)
x=[]
n=int(input("ENTER THE NUMBER OF SUBJECTS :"))
for i in range(0,n):
    o=int(input("ENTER THE MARKS OF SUBJECT:"))
    x.append(o)
average_of_marks() #function is called''' 

#write a funtion to convert indian rupee into us dollar and take the input from the user 

'''def conversion_currency_INR_to_USD(x):  #function name -conversion_currency_INR_to_USD(x) and it converts inr to usd 
    print("INR TO USD :INR",x*81.09)
def conversion_currency_USD_to_INR(y):  #function name -conversion_currency_INR_to_USD(x) and it converts usd to inr
    print("USD TO INR :$",y/81.09,)

x=int(input("ENTER THE MONEY IN INR :"))
y=int(input("ENTER THE MONEY IN USD :"))
conversion_currency_INR_to_USD(x)  #function is called   
conversion_currency_USD_to_INR(y)  #function is called''' 

#write a funtion to calculate the fibonacci series and factorial of a number without recursion
'''def fibonacci(n):   #function name - fibonacci(n) and it calculates the fibonacci series  
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def factorial(n): #function name - factorial(n) and it calculates the factorial of the number  
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        print(fact, end=" ")
    print()

n = int(input("Enter n: "))
fibonacci(n) #function is called.
factorial(n) #function is called.'''


#Recursion can be defined as when the function calls itself repeatedly in itself
#loops and recusion are always interelated , which means loop<------>recursion

#write a funtion to calculate the fibonacci series and factorial of a number with the help of recursion
'''def fact(f):
    if f == 0 or f == 1:
        return 1
    else:
        return f * fact(f - 1)    #calculating factorial using recursion

def fib(f):
    if f <= 1:
        return f
    else:
        return fib(f - 1) + fib(f - 2)    #calculating fibonacci series using recursion

r = int(input("ENTER THE NUMBER: "))
print("FACTORIAL OF THE NUMBER IS:", fact(r))
print("FIBONACCI SERIES UP TO THE NUMBER:")
for i in range(r):
    print(fib(i), end=" ")'''

#write a function to calculate the sum of numbers till n natural number:

'''def sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

x = int(input("ENTER A NUMBER: "))
result = sum(x)
print("SUM =", result)'''

#write a funtion to print all the elements of the list in the single line

'''def print_list(l):
    for i in range(0,len(l)):
        print(l[i],end=" ")
l=[]
n=int(input("ENTER THE NUMBER OF elements in the list :"))

for j in range(0,n):
    s=input("ENTER THE ELEMENT:")
    l.append(s)
print_list(l)'''

