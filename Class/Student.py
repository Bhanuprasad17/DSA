


# class Student:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def showInfo(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)

# obj = Student("Bhanuprasad",23)
# obj.showInfo()




class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def display(self):
        print('Name :',self.name)
        print('Age',self.age)


obj =  Student('Bhanu',23)
obj2 = Student('dell',7)
obj.display()
obj2.display()