# (Q)Store the following word meaning in the dictionary and print the dictionary
# Table:"A piece of furniture", "list of facts and figures", cat:"a small animal" 

'''dict1={}
dict1["Table"]=["a piece of Furniture","list of facts and figures"]
dict1["cat"]="A small animal"
print(dict1)'''


# (Q)You are given number of subjects and note that each subject require one class room.
#calculate the number of classroom required 
#subjects : [python,java,c++,c++,java,javascript,python,java,javascript,react,nodejs,html,css]

'''set1={"python","java","c++","c++","java","javascript","python","java","javascript","react","nodejs","html","css"}
sorted_set=set(set1)
print("NUMBER OF CLASSES REQUIRED PER SUBJECT IS :",len(sorted_set))'''


#write a python program to take the input of the 3 subject marks from the user in a dictionary, use subject as value and marks as keys , note that take an empty dictionary and then add one by one

'''marks={}
x=int(input("ENTER THE MARKS OF PHYSICS:"))
y=int(input("ENTER THE MARKS OF CHEM:"))
z=int(input("ENTER THE MARKS OF MATHS:"))
marks.update({"PHY":x,"CHEM":y,"MATH":z})
print("MARKS OF THE STUDENT:",marks)'''

#write a python prograam to store a 9 and 9.0 into the set 

#method 1
'''null_set=set()
null_set.add(9)
null_set.add("9.0")
print(null_set)'''


#method 2
'''a=set()
a.add(("Float",9.0))
a.add(("integer",9))
print(a)'''