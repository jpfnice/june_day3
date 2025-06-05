import math

class Point:   # __new__(), __init__() __repr__() __eq__() __setattr__()

    def __init__(self, valX, valY):
        if isinstance(valX, int):
            self.x=valX
        else:
            self.x=0
        if isinstance(valY, int):
             self.y=valY
        else:
             self.y=0
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x+other.x, self.y+other.y)
        if isinstance(other, int):
            return Point(self.x+other, self.y+other)
    def distance(self, other):
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __setattr__(self, name, value):
        if name in ["x", "y"] and isinstance(value, int):
            self.__dict__[name]=value
        else:
            print("Wrong argument received")
        

center=Point("abc",0) 
print(center.__dict__)
# 1) center=Point.__new__()
# 2) center.__init__(0,0)
# 3) __init__(center, 0, 0)

print(center) # <0,0>
# 1) print(center.__repr__())
print("center.x is", center.x)
print("center.y is", center.y)

center.x="abc" # center.__setattr__("x","abc")
center.y=4 # center.__setattr__("y",4)
center.z=6 # center.__setattr__("z",6)
print(center.__dict__)

print(center) # <5,4>

p2=Point(2,1)
print("p2 is", p2)

p3=center+p2
# 1) p3=center.__add__(p2)

print("p3 is", p3) # <7,5>

p3=p3+10
# 1) p3=p3.__add__(10)

print("p3 is", p3)# <17,15>

d=p2.distance(p3)
print(d)
print("p2:", p2)
p3.x=2
p3.y=5
print("p3:", p3)

if p2 == p3: # if p2.__eq__(p3):
    print("Equal")
else:
    print("Different")





