class sphere :
    def __init__(self,radius) :
        self.pi = 3.14
        self.radius = radius

    def area(self) :
        return (4*self.pi*self.radius**2)

    def volume(self) :
        return (4/3*self.pi*self.radius**3)


radius = int(input("please enter radius : "))
if radius >= 0 :
    try :
        s1 = sphere(radius)
        print(s1.area())
        print(s1.volume())
    except :
        print("Error")
        print(radius/0)
    finally :
        print("finished")