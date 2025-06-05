
"""
Stack:
    a stack is a collection
    a stack has a maximum size
    a push() method is provided to add a new element "on top" of the Stack
    a peek() method is provided to get the value of the element "on top" of the 
    Stack
    a pop() method is provided to get the value and remove the element "on top" 
    of the Stack
    ...
    
Attributes:
    The maximum size of the stack: an int
    The elements stored in the stack: a list
"""


class stack: # __init__ __repr__
    def __init__(self, maximum):
        # TO BE COMPLETED: 
        # __init__ normally takes care of initializing the attributes
        pass
    def push(self, value):
        # 1) Is there some space available in self ?
        # 2) If Yes, then we have to "store" value into Stack
        # 3) if No, then we print an error message
        # TO BE COMPLETED
        pass
    def __repr__(self):
        # returns a string representation of self
        # TO BE COMPLETED
        pass
    def __len__(self):
        # returns the number of element of self
        # TO BE COMPLETED
        pass
    def peek(self):
        # 1) Is there one or more element in self ?
        # 2) If Yes, then return the last element of self
        # 3) if No, then we print an error message
        # TO BE COMPLETED
        pass
    def pop(self):
        # 1) Is there one or more element in self ?
        # 2) If Yes, then return and remove the last element of self
        # 3) if No, then we print an error message
        # TO BE COMPLETED
        pass
    def isEmpty(self):
        # 1) Is there one or more element in self ?
        # 2) If Yes, then return True
        # 3) if No, then return False
        # TO BE COMPLETED
        pass
    
s1=stack(10) # a stack with a maximum size of 10 elements
s1.push(45) # push(s1, 45)
s1.push(567)
s1.push(8)
print(s1) # (3/10) [45,567,8]
print(len(s1)) # 3 # len(s1) => s1.__len__()
top=s1.peek() 
print(top) # 8
top=s1.peek() 
print(top) # 8
print(s1) # (3/10) [45,567,8]
top=s1.pop() 
print(top) # 8
print(len(s1)) # 2 
print(s1) # (2/10) [45,567]
top=s1.pop() 
print(top) # 567
print(len(s1)) # 1 
print(s1) # (1/10) [45]

