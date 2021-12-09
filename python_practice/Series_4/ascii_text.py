import os
import shutil
directory = input("please enter your directory : ")
l = os.listdir()
os.makedirs(directory + "\\folder")
for i in l :
    if "a" in i and len(i) == len(ascii(i)):
        shutil.copyfile(directory + "\\" + i , directory + "\\folder" + i)