#روش اول

lst = [ 1000, 500, 600, 700, 5000, 90000, 175000]

def add_2000(item) :
    if item < 8000 :
        return (item + 2000)
    else :
        return item

result = map(add_2000, lst)
lst_result = []
for x in result :
    lst_result.append(x)
print(lst_result)

#-----------------------------------------------
#روش دوم

print(list(map(add_2000, lst)))

#-----------------------------------------------
#روش سوم

lst_result = []
for item in lst :
    result = lambda item : add_2000(item)
    lst_result.append(result)
print(lst_result)
