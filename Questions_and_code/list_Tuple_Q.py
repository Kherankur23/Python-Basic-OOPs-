#write a python code to take 3 input from the user of its number and append it into the list:

'''list=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS YOU WANT TO ADD:"))
for i in range(0,n):
    x=int(input("ENTER THE NUMBER YOU WANT TO ADD INTO THE LIST:"))
    list.append(x)
print(list)'''

#Write a python code to check if the list contains palindrome number or not.
#note that:palindrome numbers are those numbers that are the same even if they are reversed in order.

'''list1=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS YOU WANT TO ADD :"))
for i in range(0,n):
    x=int(input("ENTER THE NUMBER:"))
    list1.append(x)
list2=list1.copy()
list2.reverse()
if (list1==list2):
    print("THE GIVEN LIST IS A PALINDROME LIST")
else:
    print("THE LIST DOES NOT COANTAIN PALINDROME NUMBER.")'''


#take a string in a list and count the number of a's in the list and print it:

'''list1 = []
n = int(input("ENTER THE NUMBER OF STRINGS YOU WANT TO ADD INTO THE LIST: "))
for i in range(n):
    x = input("ENTER THE STRING YOU WANT TO ADD: ")
    list1.append(x)

print(list1)
count_A = sum(s.count("A") for s in list1)
count_a = sum(s.count("a") for s in list1)

print("THE NUMBER OF TIMES 'A' HAS OCCURRED IN THE LIST IS:", count_A)
print("THE NUMBER OF TIMES 'a' HAS OCCURRED IN THE LIST IS:", count_a)'''

#sort the grades that are placed in the list:

'''list1=[]
n=int(input("ENTER NUMBER OF GRADES YOU WANT TO ADD IN THE LIST:"))
for i in range(0,n):
    x=input("ENTER THE GRADE :")
    list1.append(x)
list1.sort()
print(list1)'''





