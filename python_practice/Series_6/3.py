# روش اول

List = [ -1000, 500, -600, 700, 5000, -90000, -175000]

ABS=list(map(lambda  lst :abs(lst),List))

result=list(map(lambda lst : abs(lst),filter(lambda x : (x<0),List)))

print(ABS)
print(result)

#--------------------------------------------------------
# روش دوم


lst = [-1000, 500, -600, 700, 5000, -90000, -175000]

def func(x) :
    if x < 0 :
        return True
    else :
        return False

result = filter(func, lst)

result_lst = []
for i in result :
    result_lst.append(abs(i))

print(result_lst)