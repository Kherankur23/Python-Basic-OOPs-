#list------------>MUTABLE DATATYPE
int_list=[1,2,3,4,5,5] #list containg integers values
float_list=[3.31,34.41,23.33,12.321] #list containing float values.
string_list=["bob","rick","sam","poo"]  #list containg string values.
print(int_list) #whole list printed
print(float_list) #whole list printed
print(string_list) #whole list printed

print("THE LENGTH OF THE STRING WITH IS:",len(string_list)) #printing the length of the list


list2=int_list+string_list #concatenation of the list method 1 {joining two list into one single list}
print("CONCATENATION METHOD 1:",list2)

list10=int_list*3
print("CONCATENATION METHOD 2:",list10)

#INDEXING IN LIST

list3=['hello','my','name is bob']
print("BEFORE CHANGING THE ELEMENT :",list3)
list3[2]="name is rohan"
print("AFTER CHANGING THE ELEMENT:",list3)


#slicing in list

list4=[1,2,3,4,5,6,7,8,9,10]
print("ELEMENTS OF LIST FROM 0 TO 3:",list4[0:3])
print("ELEMENTS OF LIST FROM 3 TO 6:",list4[3:6])
print("ELEMENTS OF LIST FROM 6 TO 9:",list4[6:9])
print("ELEMENTS OF LIST FROM 9 TO len(list4):",list4[9:])
print("ELEMENTS OF LIST FROM 0 TO len(list4) and STEP VALUE=2:",list4[0::2])
print("ELEMENTS OF LIST FROM 0 TO 3 and STEP VALUE=3:",list4[3:6:3])
print("REVERSE OF THE LSIT IS :",list4[::-1])

#methods in list:

list1=[] #empty list
n=int(input("ENTER THE NUMBER OF ELEMENTS YOU WANT TO ADD IN THE LIST:"))
for i in range(0,n):
    num=int(input("ENTER THE NUMBER YOU WANT TO ADD IN THE LIST:"))
    list1.append(num)  #THIS INSERTS THE ELEMENTS INTO THE LIST
sort_asc=list1.sort()
sort_desc=list1.sort(reverse=True)
print("SORTED FORM THE LIST IN ASCENDING ORDER :",sort_asc) #SORTS THE LIST INTO ASCENDING ORDER
print("SORTED LIST IN DESCENDING ORDER IS :",sort_desc) #sorts the list into descending order.
list1.insert(n+1,10) #inserts the element at the n+1 posting and the element inserted is 10
#print(list1)
list1.remove(10) #this will remove the number 10 at its first occurence
list1.pop(3)  #this will delete the element that is present in the index postion 3
print(list1)


