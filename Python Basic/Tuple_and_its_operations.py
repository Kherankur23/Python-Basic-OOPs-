#basic of Tuple-------->IMMUTABLE DATATYPE
tuple1=(1,2,3,4,5,6,7)
tuple2=("HELLO","WORLD","PYTHON","C++")
print(tuple1)
print(tuple2)

tuple_empty=() #THIS IS AN EMPTY TUPLE.


#VARIOUS METHODS IN TUPLE

t1=(1,2,3,4,5,3,3,3,"hello","world","python","c++")
print("THE INDEX POSITION OF HELLO IS :",t1.index("hello"))  #will return the index postion of the first occurence of the word/integer.
print("THE NO OF TIMES 3 HAS OCCURED IN THE TUPLE IS:",t1.count(3)) #will count and return the number of times 3 has occured in the given tuple 

#INDEXING IN TUPLE IS AS SAME AS IN THAT OF STRING AND LIST
#SLICING IN TUPLE IS AS SAME AS IN THAT OF STRING AND LIST
#most of the methods are also same use as you wish or as needed
#concatenation in tuple there are two methods

tup1=(1,2,3,4,5)
tup2=(6,7,8,9,10)
tup3=tup1+tup2
print("CONCATENATION METHOD 1:",tup3)
tup4=tup1*3

