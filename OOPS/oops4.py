#HERE , THE CLASS NAME=XYZ IS NOT CHANGED AND THE OUTPUT WILL BE RAHUL AND XYZ
'''class Person:
    name="XYZ"

    def change_name(self,name):
        self.name=name
p1=Person()
p1.change_name("RAHUL")
print(p1.name)
print(Person.name)'''

#HERE , THE CLASS NAME=XYZ IS CHANGED ACCORIND TO THE INPUT AND THE OUTPUT WILL BE RAHUL AND RAHUL
#METHOD 1:
'''class Person:
    name="XYZ"

    def change_name(self,name):
        Person.name=name
p1=Person()
p1.change_name("RAHUL")
print(p1.name)
print(Person.name)'''


#HERE , THE CLASS NAME=XYZ IS NOT CHANGED AND THE OUTPUT WILL BE RAHUL AND RAHUL
#Method 2:

'''class Person:
    name="XYZ"

    def change_name(self,name):
        self.__class__.name=name
p1=Person()
p1.change_name("RAHUL")
print(p1.name)
print(Person.name)'''


#HERE , THE CLASS NAME=XYZ IS NOT CHANGED AND THE OUTPUT WILL BE RAHUL AND RAHUL
#Method 3: {using the class method:}

'''class Person:
    name="XYZ"
    
    @classmethod    #class method decorater
    def change_name(cls,name):
        cls.name=name
p1=Person()
p1.change_name("RAHUL")
print(p1.name)
print(Person.name)'''

