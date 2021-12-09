class Rectangle :
    def __init__(self,length,width) :
        self.length = length
        self.width = width
        print("\t"," _" * self.length)
        for i in range(self.width) :
            print("\t","|"+" "*2*self.length+"|")
        print("\t"," _" * self.length)

    def func(self) :
        print("\tEnvironment =",2*(length+width))
        print("\tarea =",length*width)

#-------------------------------------------------

length = int(input("please enter length of Rectangle : "))
width = int(input("please enter width of Rectangle : "))
object1 = Rectangle(length,width)
object1
object1.func()
