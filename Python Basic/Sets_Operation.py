#Set : It can be defined as a unique collection of unordered data, in a set each element is unique and its immutable
nums={1,2,3,4,5,6,2,1,22,34,21}
print("set 1 :",nums)  # as you can see in the output the duplicated values are only displayed once , they are not repeated
null_set=set() #this will create a null set 
#note that a set can contain tuple, string but it cannot contain list and dictionary.
set2={"HELLO",1,2,3,4,5,("PYTHON","C++")}
print("set 2 :",set2)

#Lets understand the methods that we use in sets :
set2.add(7)
print("Adding elements in the set :",set2)
set2.remove(3)
print("Removing  element from the set :",set2)
print("Poping a random value from the set :",set2.pop())
print("set 2 after all the operation :",set2)
print("CLEARING THE SET THAT IS MAKING THE SET EMPTY",set2.clear())

#More Methods in Sets:
set3={1,2,3,4,5}
set4={5,6,7,8,9,10}
print("THE UNION OF THE SET IS :",set3.union(set4))
print("INSETSECTION OF THE SET IS :",set3.intersection(set4))