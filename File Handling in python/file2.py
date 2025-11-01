#METHOD 1:
f=open("C:\VS CODE\Python Programs\File Handling in python\demo2",'a')
f.write("Python is a powerful programming language that emphasizes simplicity and readability.")
f.write("\nIt supports multiple programming paradigms, including object-oriented and functional programming.")
f.seek(0)
f.close()

#METHOD 2:
'''f=open("C:\VS CODE\Python Programs\File Handling in python\demo2",'w')
f.write("Python is a powerful programming language that emphasizes simplicity and readability.")
f.seek(0)
f.write("\nIt supports multiple programming paradigms, including object-oriented and functional programming.")
f.seek(0)
f.close()
'''

