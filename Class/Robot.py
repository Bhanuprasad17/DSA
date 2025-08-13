# class Stack:
#     def __init__(self, name):
#         self.name = name   # save it in the object
    
#     def greet(self):
#         return "Hello " + self.name + " from Stack class"



# class Stack:
#     def __init__(self):
#         pass
#     def greet(self,name):
#         return "Hello " + name + " from Stack class"
    

# obj = Stack("John")

# print(obj.greet())


class Robot:
    def __init__(self, name):
        self.name = name  # store the name inside the object

    def say_hello(self):
        print("Hello, my name is", self.name)

r1 = Robot("John")
r1.say_hello()
