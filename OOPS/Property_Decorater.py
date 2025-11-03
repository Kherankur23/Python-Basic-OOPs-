class Student:
    
    def __init__(self,phy,chem,math):
        self.chem=chem
        self.phy=phy
        self.math=math
        #self.percentage=str((self.chem+self.math+self.phy)/3) + "%"
        #in the above percentage method , if suppose we change the value of any of the marks the percentage will not change accordingly


        #percentage:
    @property    #THIS IS USED FOR THE AUTOMATIC UPDATION ON THE CALULATED ATTRIBUTE
    def calc_percentage(self):
        return str((self.chem+self.math+self.phy)/3) + "%"


s1=Student(80,90,75)
print("Percentage before changing the marks :",s1.calc_percentage)

s1=Student(90,87,90)
print("Percentage After changing the marks:",s1.calc_percentage)
    

