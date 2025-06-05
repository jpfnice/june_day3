
data=[34,56,78,89,10,30]


try:
    index=input("Pleaser enter an int in the range [0,5]: ")
    index=int(index) 
    print("At position", index, "there is the element", data[index])
        
except IndexError as ex:
    print("IndexError Exception raised:", ex)
except ValueError as ex:
    print("ValueError Exception raised:", ex)
else:
    print("No exception !")
    
print("The end")
