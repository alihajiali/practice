import os
directory = input("please enter your directory : ")
directory_name = input("please enter your directory name : ")
l = os.listdir()
if directory_name in l :
    print(":)")
else :
    os.makedirs(directory + "\\" +directory_name)