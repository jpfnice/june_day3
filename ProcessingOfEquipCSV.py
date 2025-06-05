
equipments=dict() # an empty dict is created

"""

"equipment1":[12.5, 16.1, 13.5, 12.1],
"equipment2":[13.6, 14.6, ...],
...


"""

fileObj=open("equip.csv")

for element in fileObj:
    data=element.split(":")
    equipmentName=data[0]
    equipmentValue=float(data[1])
    #print(equipmentName, "->", equipmentValue)
    if equipmentName in equipments:
        equipments[equipmentName].append(equipmentValue)
    else:
        equipments[equipmentName] = [equipmentValue]
    
for k,v in equipments.items():
    print(k, v)
    
print(min(equipments["equipment3"]))
print(sum(equipments["equipment2"])/len(equipments["equipment2"]))



