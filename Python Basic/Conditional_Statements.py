#To understand the conditional statemnts lets take an example
#consider that the if marks>=90 then A , 80=<marks<90 then B,70<=marks>80 then C, else D 
# we used both conditional and looping statements and also used list this is the most efficient code


n=int(input("ENTER THE NUMBER OF SUBJECTS:"))
for i in range(0,n): 
    mark=int(input("ENTER THE MARKS OF YOUR SUBJECT :"))
    l=[]
    l.append(mark)
    average=sum(l)/len(l)

if(average>90):
    print("GRADE: S ")
elif(80<=average>90):
    print("GRADE: A")
elif(70<=average>80):
    print("GRADE: B")
else:
    print("GRADE: D")
