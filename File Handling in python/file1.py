#Method 1:
'''with open("C:\VS CODE\Python Programs\File Handling in python\demo1",'r') as f:
    data=f.read()
'''
#Method 2:
f=open("C:\VS CODE\Python Programs\File Handling in python\demo1","r")  #THe path of the file is entered and is opened in the read mode
data2=f.read(20) #THIS WILL MOVE THE FILE POINTER/CURSOR TO THE 20TH CHARACTER
f.seek(0) #THIS WILL MOVE THE FILE POINTER/CURSOR AT THE STARTING OF THE FILE
data=f.read() #this read() funtion read the whole data present in the file and the pointer to the end of the file
f.seek(0)
readline1=f.readline() #READS THE FIRST LINE AND MOVES THE POINTER AT THE END OF THE FIRST LINE
readline2=f.readline() #READS THE SECOND LINE AND MOVES THE POINTER AT THE END OF THE SECOND LINE
readline3=f.readline() #READS THE THIRD LINE AND MOVES THE POINTER AT THE END OF THE THIRD LINE
f.seek(0)
print("THE DATA IN THE FILE IS :\n",data)
print("THE FIRST 20 CHARACTERS IN THE FILE ARE :\n",data2)
print("THE FIRST LINE IN THE FILE IS :",readline1)
print("THE SECOND LINE IN THE FILE IS :",readline2)
print("THE THIRD LINE IN THE FILE IS :",readline3)
f.close() #this closes the file and its imp to close the file as it help to increase program efficiency