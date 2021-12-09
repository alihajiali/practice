import re
#---------------------------------------------------------
#---------------------------------------------------------

phone_number = input('please enter your phone number : ')

#---------------------------------------------------------
#---------------------------------------------------------

def check(phone_number) :
    if re.search('^(\+98|0098|98|0)?9\d{9}$', phone_number) :
        result = re.finditer('9\d{9}$', phone_number)
        for number in result :
            print('0'+number.group())
    else :
        print('‫‪invalid‬‬ ‫‪phone‬‬ ‫‪number‬‬')


check(phone_number)