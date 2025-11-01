#create a new file 'practice.txt' using python and add the following data into it :
'''hii everone
   We are learning File I/O
   using Java
   I like programming in Java
'''
#also write a function that replaces all the occurrence of "java"---->"Python" in the above file
#also search the word "learing" exists in the file or not

# Step 1: Create a new file and write data into it
f = open("C:\\VS CODE\\Python Programs\\Questions_and_code\\file handling q\\practice.txt", "w")
f.write("""hii everyone
We are learning File I/O
using Java
I like programming in Java
""")
f.close()

# Step 2: Function to replace all occurrences of "Java" → "Python"
def replace_word():
    f = open("C:\\VS CODE\\Python Programs\\Questions_and_code\\file handling q\\practice.txt", "r")
    data = f.read()
    f.close()

    data = data.replace("Java", "Python")  # replace all Java → Python

    f = open("C:\\VS CODE\\Python Programs\\Questions_and_code\\file handling q\\practice.txt", "w")
    f.write(data)
    f.close()

# Step 3: Function to search if "learning" exists in the file
def search_word():
    f = open("C:\\VS CODE\\Python Programs\\Questions_and_code\\file handling q\\practice.txt", "r")
    data = f.read()
    f.close()

    if "learning" in data:
        print("The word 'learning' exists in the file.")
    else:
        print("The word 'learning' does NOT exist in the file.")

# Function calls
replace_word()
search_word()


