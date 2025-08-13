class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty() == False:   # instead of: if not self.is_empty()
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0    # This is already fine ✅

    def peek(self):
        if self.is_empty() == False:   # instead of: if not self.is_empty()
            return self.items[-1]
        return None

    

# def is_valid_parentheses(s):  
#     stack = Stack()
#     parentheses_map = {')': '(', '}': '{', ']': '['}

#     for char in s:
#         if char in parentheses_map.values():  # If it's an opening bracket
#             stack.push(char)
#         elif char in parentheses_map.keys():  # If it's a closing bracket
#             if stack.is_empty() or stack.pop() != parentheses_map[char]:
#                 return False

#     return stack.is_empty()  # If stack is empty, all brackets were matched

def is_valid_parentheses(s):
    stack = Stack()

    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)

        elif char == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False

        elif char == '}':
            if stack.is_empty() or stack.pop() != '{':
                return False

        elif char == ']':
            if stack.is_empty() or stack.pop() != '[':
                return False

    return stack.is_empty()



print(is_valid_parentheses("()[]{}"))  # Should return True
print(is_valid_parentheses("(]"))  # Should return False
print(is_valid_parentheses("([{}])") ) # Should return True