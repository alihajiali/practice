import os
directory = input("please enter your directory : ")
l = os.listdir()
for i in l :
    file = directory + "\\" + i

    with open(file)as reader :
        result = reader.readlines()

with open(directory+"\\filename.txt","w") as writer :
    writer.write(result)

# "C:/Users/Ali/Desktop/python"