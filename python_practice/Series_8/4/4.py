import re

def func(txt):
#تابعی که یک متن دریافت میکند و درون متن بررسی میکند که اگر عبارات مورد نظر داخل متن بودند پیغام شد میدهد در غیر اینصورت پیغام پیدا نشد میدهد
    if re.search(r'.*(A).*(\$).*(\d+).*', txt): 
        print('The desired pattern was found.')
        
    elif re.search(r'.*(\$).*(A).*(\d+).*', txt): 
        print('The desired pattern was found.')
        
    elif re.search(r'.*(\d+).*(\$).*(A).*', txt): 
        print('The desired pattern was found.')
        
    elif re.search(r'.*(A).*(\d+).*(\$).*', txt):  
        print('The desired pattern was found.')
        
    elif re.search(r'.*(\d+).*(A).*(\$).*', txt):  
        print('The desired pattern was found.')
        
    elif re.search(r'.*(\$).*(\d+).*(A).*', txt):  
        print('found')
        
    else:
        print('not found')
    
         
txt = 'MohammadminV$erdipour65biographyispyAthonprogramming.'          
func(txt)


