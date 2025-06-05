
class listPlus (list):
    
    def removeAll(self, value):
        while value in self:
            self.remove(value)
            
    def __add__(self, list2, default=0):
        newList=[]
        if len(self) > len(list2):
            for index in range(len(list2)): 
                newList.append(self[index]+list2[index])
            for index in range(len(list2), len(self)): 
                newList.append(self[index]+default)
        else:
            for index in range(len(self)):
                newList.append(self[index]+list2[index])
            for index in range(len(self), len(list2)):
                newList.append(list2[index]+default)
        return newList 

        
l=listPlus()
l.append(12)
l.insert(0,100)
l.append(12)
l.append(12)
l.append(200)
print("list size", len(l))
print(l)
l.removeAll(12)
print("list size", len(l))
print("l is", l)

l2=listPlus()
l2.append(12)
l2.append(42)
l2.append(32)
l2.append(200)

print("l2 is", l2)

# l3=l.addList(l2)
# print("l3 is", l3)

l3=l + l2
print("l3 is", l3)

