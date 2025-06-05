import os

path=r"C:\Users\jpf\June25"

for filename in os.listdir(path):
    if len(filename) > 1:
        with open(path+"\\"+filename) as fic:
            print("first 5 line of the file", filename, "is:")
            for l in range(5):
                print(fic.readline(), end="")
