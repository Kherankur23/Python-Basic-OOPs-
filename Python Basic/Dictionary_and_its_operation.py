#Dictionary are the type of data structure that stores the data in the form of key pair value 
#They are unordered and mutable data type and every dictionary cotains unquie keys.



dict={} #this is an empty dictionary
dict1={1:"HELLO",2:"world",3:"python",4:"C++",5:"XYZ",6:['python','c++',"Js","Java"]} #THIS IS A DICTIONARY WHICH STROES THE KEY PAIR VALUE
dict1[7]="THIS IS THE ADDED KEY" #This is how we add new data into the dictionary
print("Dictionary 1 :",dict1) 
print("THE VALUE OF THE KEY WHERE KEY IS 3 IS :",dict1[3]) #accessing and printing the value of key Method 1
print("THE VALUE OF THE KEY WHERE KEY IS 4 IS :",dict.get(4)) #accessing and printing the value of the key Method 2
#The difference between method 1 and 2 is that method 2 doesnt give any kind of error if the key doesnt exist in the dictionary.
dict1[1]="CHANGED VALUE" #CHANGING THE VALUE IN THE DICTIONARY ACC TO THE KEY
print("Dictionary 1(UPDATED) :",dict1)

#NESTED DICTIONARY - It can be defined as the parent dictionary containing a child dictionary.
#lets take an exmaple :

student1={
    "name":"ROHAN",
    "Subject": {
        1:"PHY",2:"CHEM",3:"MATH",4:"ENG"
    },
    "class":7
    }
print("THE NESTED DICTIONARY IS :",student1)
#To access the nested Dictonary we can use the following :

print("ASSCESSING AND PRINTING THE NESTED DICT:",student1["Subject"][3])

#Methods in Dictionary :

print("ALL THE KEYS IN THE DICTIONARY:",dict1.keys()) #return the key in the dictionary
print("ALL THE VALUE IN THE DICTIONARY:",dict1.values()) #returns the value in the dictionary
print("TOTAL NUMBER OF KEYS IN A DICTIONARY:",len(dict1))#returns the number of keys in dictionary
print("ITEMS OF THE DICTIONARY{FULL DICTIONARY}:",dict1.items()) #returns all the key value pair in the form of tuple
student1.update({"Adddress":["Mumbai","Delhi","Pune"]}) #THIS WILL UPDATE THE DICTIONARY AN ADD ANOTHER DICTIONARY INTO THE STUDENT1
print("THE NESTED DICTIONARY(UPDATED) IS:",student1)








