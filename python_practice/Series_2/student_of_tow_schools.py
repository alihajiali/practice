class schools :
    def __init__(self , n) :
        self.n = n
        self.age = input("please enter age of students : ").split()
        self.height = input("please enter height of students : ").split()
        self.weight = input("please enter weight of students : ").split()

    def func_age(self) :
        self.age1 = 0
        for i in self.age :
            self.age1 += int(i)
        return self.age1 / self.n

    def func_height(self) :
        self.height1 = 0
        for i in self.height :
            self.height1 += int(i)
        return self.height1 / self.n

    def func_weight(self) :
        self.weight1 = 0
        for i in self.weight :
            self.weight1 += int(i)
        return self.weight1 / self.n


#--------------------------------------------------------------

n = int(input("please enter number of students of school1 : "))
school1 = schools(n)
n = int(input("please enter number of students of school2 : "))
school2 = schools(n)

print(school1.func_age())
print(school1.func_height())
print(school1.func_weight())

print(school2.func_age())
print(school2.func_height())
print(school2.func_weight())

#--------------------------------------------

if school1.func_height() > school2.func_height() :
    print("A")
elif school1.func_height() < school2.func_height() :
    print("B")
else :
    if school1.func_weight() < school2.func_weight() :
        print("A")
    elif school1.func_weight() < school2.func_weight() :
        print("B")
    else :
        print("Same")
