"""
a dict is a mutable collection (a dict is an iterable object)

"""
phone={"mario":45676, 
       "julia":89876, 
       "yohan":76554}

print(len(phone), type(phone))

# phone={45676, 
#        89876, 
#        76554}

# print(len(phone), type(phone))

if "Yohan" in phone:
    print("Phone number of yohan", phone["Yohan"])
else:
    print("The key Yohan does not exist")
print("Phone number of julia", phone["julia"])

phone["yohan"]=67665

print("Phone number of yohan", phone["yohan"])

if "jean" in phone:
    print("Phone number of yohan", phone["jean"])
    
print(phone) 
   
phone["louis"]=98889

print(phone)

#del phone["julia"]
# <=>
phone.pop("julia")


phone["julie"]=98889

print(phone)

for e in phone:
    print(e)
    
for k in phone.keys():
    print(k)

for k in phone.values():
    print(k)
    
for k,v in phone.items():
    print(k, v)
    
print("Value associated with the key julie:", phone.get("Julie"))
print("Value associated with the key julie:", phone["Julie"])
    
