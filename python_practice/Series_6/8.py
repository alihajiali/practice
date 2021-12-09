def duble_result(func):
    def wrapper(*args):
        return func(*args) * 2
    return wrapper
        

@duble_result
def myFunction(a, b):
    return (a+b)

print(myFunction(5, 5))
