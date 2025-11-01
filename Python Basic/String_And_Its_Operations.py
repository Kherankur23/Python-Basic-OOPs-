#STRING-------->IMMUTABLE DATATYPE
#BASIC OF THE STRING#

a='HELLO WORLD!\n'  #single semi colon used hence Best for simple, one-line strings.
b="HELLO WORLD!\n"  #double semi colon used hence Functionally the same as single quotes.
c="""HELLO WORLD!\n""" #triple semi colon used to write multiline strings.
print("SINGLE QUOTE STRING:",a)
print("DOUBLE QUOTE STRING:",b)
print("TRIPLE QUOTE STRING:",c)


#USE OF THE \n IN THE STRING #

d="HELLO PYTHON WORLD,\nWE ARE HAPPPY TO INFORM YOU THAT THIS IS A STRING. "
#"\n" THIS ALLOWS THE USER TO PRINT THE STRING INTO THE DIFFRENT LINE
print(d)



#CONCATENATION OF THE STRING AND ITS VARIOUS METHODS

e="HELLO" + " " +"World!!"  #THIS IS CALLED CONCATENATION OF THE STRING.
print("CONTATENATION OF DIFFERENT STRING IS(METHOD 1) :",e)
#THERE ARE GENERALLY TWO TO THREE METHODS WHICH ARE GIVEN BELOW.
str1,str2="RICK","MORTY"
str3=str1+" "+"AND"+" "+str2
print("CONTATENATION OF DIFFERENT STRING IS(METHOD 2) :",str3)

str4="HELLO"
str5=str4*3
print("CONTATENATION OF THE SAME STRING  IS(METHOD 3) :",str5)


#FINDING THE LENGTH OF THE LIST , len()

str6="HELLO "
len1=len(str6)
print("THE LENGTH OF THE STRING IS :",len1)


#INDEXING IN STRNG : IT ALLOWS US TO ACCESS AND PRINT THE CHARACTERS OF THS STRING.

str8="HELLO"
print("THE FIRST ELEMENT OF THE STRING:(NOTE::str8[0]==str8[-5]):",str8[0])
print("THE SECOND ELEMENT OF THE STRING:(NOTE::str8[1]==str8[-4]):",str8[1])
print("THE THIRD ELEMENT OF THE STRING:(NOTE::str8[2]==str8[-3]):",str8[2])
print("THE FOURTH ELEMENT OF THE STRING:(NOTE::str8[3]==str8[-2]):",str8[3])
print("THE FIFTH ELEMENT OF THE STRING:(NOTE::str8[4]==str8[-1]):",str8[4])

#SLICING THE STRING{AND ALSO REVERSING THE STRING}
#SYNTAX : String_Name[Starting index:Ending index:Step value]

str9="HELLOPYTHONWORLD!!!!"
slice1=str9[0:3]
slice2=str9[3:6]
slice3=str9[6:9]
slice4=str9[9:12]
slice5=str9[0:3:3]
slice6=str9[0:3:5]
slice7=str9[0:3:]
slice8=str9[::-1]
print("THE ELEMENTS FROM INDEX 0 TO 3 ARE :",slice1)
print("THE ELEMENTS FROM INDEX 3 TO 6 ARE :",slice2)
print("THE ELEMENTS FROM INDEX 6 TO 9 ARE :",slice3)
print("THE ELEMENTS FROM INDEX 9 TO 12 ARE :",slice4)
print("THE ELEMENTS FROM INDEX 0 TO 3 AND A STEP VALUE OF 3 ARE :",slice5)
print("THE ELEMENTS FROM INDEX 0 TO 3 ARE A STEP VALUE OF 5 ARE :",slice6)
print("THE ELEMENTS FROM INDEX 0 TO 3 ARE A STRP VALUE OF 0 ARE :",slice7)
print("THE STRING IF REVERSED ITS AS FOLLOWS:",slice8)


#SOME MORE FUNCTION OF THE STRING:
str10="i am a coder."
print("TO CHECK IF THE STRING ENDS WITH (er) or not ?:",str10.endswith("er."))  #returns true or flase as a ans
print("STRING AFTER capitalize() FUCNTION {FIRST LETTER WILL BE CAPITAL}:",str10.capitalize())
print("TO FIND THE WORD CODER IS PERESENT OR NOT? AND IF YES THEN THE INDEX OF ITS FIRST OCCURENCE IS AS FOLLOWS::",str10.find("coder")) #returns true or flase as a ans
print("TO COUNT THE NUMBER OF TIMES a HAS OCCURED IN THE STRING:",str10.count("a")) 
print("REPLACING THE coder to python coder then the string becomes:",str10.replace("coder","python coder"))
print("ORIGINAL STRING :",str10)
#note that these changes are not done in the orginal string , the original strings stays intact as string datatype is an immutable datatype

#ACCESSING AND PRINITNG EACH AND EVERY ELEMENT OF THE STRING USING FOR LOOP:
str11="GOODMORNING EVERYONE MY NAME IS SAM"
X=len(str11)
for i in range(0,X):
    print(str11[i],end=" ")