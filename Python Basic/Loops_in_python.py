#Loops : it can be defined as a key word which is used to repeat any instrution in a given code

# (Q)
# print number from 1 to 100:
'''i=0
while i<=100:
    print(i)
    i+=1'''

'''for i in range(0,101):
    print(i)'''

# (Q) print number from 100 to 1:
'''i=100
while i>=1:
    print(i)
    i-=1'''

'''for i in range(100,0,-1):
    print(i)'''

# (Q) print the multiplication table till number 20 of the number n

'''n=int(input("ENTER THE NUMBER YOU WANT THE TABLE TILL 20 FOR:"))
i=1
while i<=20:
    print(n*i)
    i+=1'''

'''n=int(input("ENTER THE NUMBER U WANT THE TABLE TILL 20 FOR :"))
for i in range(0,21):
    print(n*i)'''

# (Q) print the elements of the following list using loops

'''a=[1,2,3,4,5,6,1,6,5,2,3]
a=len(a)
i=0
while i<=a:
    print(i)
    i+=1'''


'''a=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(a)):
    print("LIST :",i)'''

# (Q) search for the number X in the tuple

'''x=int(input("ENTER THE NUMBER YOU WANT TO CHECK:"))

y=(1,2,3,4,5,6,7,8.9,10,11,12,13,14,15)
i=0
while i<len(y):
    if( y[i] == x):
        print("NUMBER FOUND AT INDEX :",i)
    else:
       print("NUMBER NOT FOUND)
    i+=1'''


'''x=int(input("ENTER THE NUMBER YOU WANT TO CHECK:"))
y=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
for i in range(0,len(y)):
    if y[i]==x:
        print("NUMBER FOUND At index :",i)
        break
    else:
        print("NOT FOUND")'''



#Break Statement : This statement is used when we have to terminate the loop at a after the specific condition
#Continue Statment : This statement is used when we have to skip the given condition in the loop and print forward
#lets take an example :

'''i=0
while i<=10:
    print(i)
    if i==3:
        break  #THE LOOP WILL TERMINATE WHEN THE CONDITION IS TRUE 
    i+=1
print("END OF LOOP")'''

'''i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1'''


#find the factorial of the number till n :

'''n=int(input("ENTER THE NUMBER YOU WANT THE FACTORIAL FOR:"))

for i in range(0,n+1):
    print(i*i+1)'''









    






