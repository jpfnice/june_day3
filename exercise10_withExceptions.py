
# StackError is an Exception
class StackError(Exception):
    pass

# StackSizeError is a StackError and by transitivity it is also an Exception
class StackSizeError(StackError):
    pass

# StackFullError is a StackError and by transitivity it is also an Exception
class StackFullError(StackError):
    pass

# StackEmptyError is a StackError and by transitivity it is also an Exception
class StackEmptyError(StackError):
    pass

class stack: 
    
    def __init__(self, maximum): 
        if isinstance(maximum, int) and maximum > 0:
            self.maxi=maximum
        else:
            raise StackSizeError(f"Invalid Stack size: {maximum} !")
            
        self.elements=[]
        
    def push(self, value):
      
        if len(self.elements) < self.maxi:
            self.elements.append(value)
        else:
            raise StackFullError(f"The Stack is full, {value} is not pushed!")
            
    def __repr__(self):
        return f"({len(self.elements)}/{self.maxi}) {self.elements}"
    
    def __len__(self):
        return len(self.elements)
    
    def peek(self):
        if len(self.elements) > 0:
            return self.elements[-1]
        else:
            raise StackEmptyError("The Stack is empty!")
        
    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop()
        else:
            raise StackEmptyError("The Stack is empty!")
        
    def isEmpty(self):
        return len(self.elements) == 0
    
try:
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
except StackEmptyError as ex:
    print("Exception:", ex)
except StackFullError as ex:
    print("Exception:", ex)
except StackSizeError as ex:
    print("Exception:", ex)

