import re
#-------------------------------------
#-------------------------------------

s = input('please enter your string : \n')
w = input('please enter your word :')

#-------------------------------------
# روش اول

# re.search('$'...)

def func(string, word) :
    if re.search(word+'$', string) :
        print('hast')
    else :
        print('nist')

func(s, w)

#-------------------------------------
# روش دوم

# re.search('\Z'...)

def func(string, word) :
    if re.search(word+'\Z', string) :
        print('hast')
    else :
        print('nist')

func(s, w)
