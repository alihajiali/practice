# روش اول )




# import os 
# from pynput import keyboard

# def on_release(key):
#     if key == keyboard.Key.enter :
#         print(reader.readline())
#     elif key == 'n' :
#         reader.close()   
#     else : 
#         print(reader.readline())

# adress = input('please enrer adress of your directory : ')
# files = os.listdir(adress)
# for file in files :
#     if '.' in file :
#         print(file)

# print('\n'+'*&^'*20+'\n')


# for file in files :
#     if '.' in file :
#         print(file)
#         with open(adress+'\\'+file , 'r') as reader :
#             print(reader.readline())
            
#             with keyboard.Listener(on_release = on_release) as Listener :
#                 Listener.join()

#                 Listener = keyboard.Listener(on_release = on_release)

#             Listener.start()

#             print('\n'+'*&^'*20+'\n')




#-------------------------------------------------------

# روش دوم )




import os

adress = input('please enrer adress of your directory : ')
files = os.listdir(adress)
for file in files :
    if '.' in file :
        print(file)

print('\n'+'*&^'*20+'\n')


for file in files :
    if '.' in file :
        print(file)
        with open(adress+'\\'+file , 'r') as reader :
            print(reader.readline())

            entry = input()
            if entry == "" :
                check = True
                while check == True :
                    print(reader.readline())
                    entry = input()
                    if entry == "" :
                        check = True
                    elif entry == "n" :
                        check = False
                    else :
                        check = True


