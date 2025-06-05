
fileObj=open("data1.txt")

for line in fileObj:
    if line=="\n":
        continue
    data=line.split(":")
    if len(data) != 2:
        continue
    print(data)
        
