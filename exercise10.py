
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
    The maximum size of the stack: "maxi" an int
    The elements stored in the stack: "elements" a list
"""

class stack: 
    # Special methods provided by default by Python (they could redefined if needed):
    #   __new__(), __init__(), __repr__(), __eq__() __ne__()
    
    def __init__(self, maximum): 
        # __init__ normally takes care of initializing the attributes
        if isinstance(maximum, int) and maximum > 0:
            self.maxi=maximum
        else:
            print("Wrong size given")
            self.maxi=10
        self.elements=[]
        
    def push(self, value):
        # 1) Is there some space available in self ?
        # 2) If Yes, then we have to "store" value into Stack
        # 3) if No, then we print an error message
        if len(self.elements) < self.maxi:
            self.elements.append(value)
        else:
            print("The stack is full: push will not work !")
            
    def __repr__(self):
        # returns a string representation of self: Ex: (3/10) [45,567,8]
        return f"({len(self.elements)}/{self.maxi}) {self.elements}"
    
    def __len__(self):
        # returns the number of element of self
        return len(self.elements)
    
    def peek(self):
        # 1) Is there one or more element in self ?
        # 2) If Yes, then return the last element of self
        # 3) if No, then we print an error message
        if len(self.elements) > 0:
            return self.elements[-1]
        else:
            print("The stack is empty: peek will not work !")
            return None
        
    def pop(self):
        # 1) Is there one or more element in self ?
        # 2) If Yes, then return and remove the last element of self
        # 3) if No, then we print an error message
        if len(self.elements) > 0:
            return self.elements.pop()
        else:
            print("The stack is empty: pop will not work !")
            return None
        
    def isEmpty(self):
        # 1) Is there one or more element in self ?
        # 2) If Yes, then return True
        # 3) if No, then return False
        return len(self.elements) == 0
    
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
top=s1.pop() 


