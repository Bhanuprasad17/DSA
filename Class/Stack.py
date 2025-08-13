

class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)    
        print(f"Pushed {item} onto the stack.")

    def pop(self):    
        if self.items == []:
           return "Stack is empty, cannot pop."
        return self.items.pop()
    
    def peek(self):
        if self.items == []:
            return "Stack is empty, cannot peek."
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print("Current stack items:", self.items)


my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.display()


print("Top item is:", my_stack.peek())
print("Popped item is:", my_stack.pop())
print("Stack size is:", my_stack.size())
print("Is stack empty?", my_stack.is_empty())
