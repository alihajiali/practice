import os
directory_name = input("please enter your directory name : \n")
l = os.listdir()
file = list()
folder = list()
for x in l :
    for i in range(len(x)) :
        if "." in x[i] :
            file.append(x)
        else :
            folder.append(x)

print(file)
print(folder)

print("number of file is : ",len(file))
print("number of folder is : ",len(folder))
