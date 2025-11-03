class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def show_Number(self):
        print(self.real,"+",self.img,"i")
    
    def __add__(self,num2):  #THIS IS A DUNDER FUNCTION FOR ADDITION
        newReal=self.real+num2.real
        newIMG=self.img+num2.img
        return Complex(newReal,newIMG)
      
    def __sub__(self,num2):  #THIS IS A DUNDER FUNCTION FOR SUBSTRACTION
        newReal=self.real-num2.real
        newIMG=self.img-num2.img
        return Complex(newReal,newIMG)
    
    def __mul__(self,num2):  #THIS IS A DUNDER FUNCTION FOR MULTIPLICATION
        # Correct complex multiplication: (a+bi)*(c+di) = (ac-bd) + (ad+bc)i
        newReal=(self.real*num2.real) - (self.img*num2.img)
        newIMG=(self.real*num2.img) + (self.img*num2.real)
        return Complex(newReal,newIMG)
    
    def __truediv__(self,num2):  #THIS IS A DUNDER FUNCTION FOR DEVISION
        # Correct complex division: (a+bi)/(c+di) = [(ac+bd)/(c^2+d^2)] + [(bc-ad)/(c^2+d^2)]i
        denominator=(num2.real**2) + (num2.img**2)
        newReal=((self.real*num2.real) + (self.img*num2.img)) / denominator
        newIMG=((self.img*num2.real) - (self.real*num2.img)) / denominator
        return Complex(newReal,newIMG)

num1=Complex(3,4)
num1.show_Number()

num2=Complex(7,4)
num2.show_Number()

num3=num1+num2
num3.show_Number()

num4=num1-num2
num4.show_Number()

num5=num1*num2
num5.show_Number()

num6=num1/num2
num6.show_Number()