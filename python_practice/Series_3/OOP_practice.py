import random
class Game :
  space = 500 
  def __init__(self,name,height,weight) :
    self.name = name
    self.height = height
    self.weight = weight
    self.lst = []
  def func(self) :
    # مشخصات ورزشکار و خطای ورزشکار داخل لیست ذخیره میشوند
    self.Coefficient = (int(random.uniform(0.5,2)*100))/100
    self.lst.append(f"the wrong of {self.name} with {self.height}cm height and {self.weight}kg weight and {self.Coefficient} Coefficient is")
    self.lst.append((self.height - self.weight)*self.Coefficient)
    return self.lst
# لیست بازگشتی هر شی از کلاس بالا در یک لیست ذخیره میشود
l = []
for i in range(1,6) :
  obj = Game(input(f"please enter name of player{i} : "),int(input(f"please enter height of player{i} : ")),int(input(f"please enter weight of player{i} : ")))
  l.append(obj.func())
# لیست شامل همه لیست هاپرینت میشود
print("\n\n\n",l,"\n\n\n")

#------------------------------------------------------------

# لیست بالا را به ترتیب نزولی مرتب میکنیم و در یک دیکشنری ذخیره میکنیم
class Db :
  def __init__(self,l) :
    self.l = l
    self.dic = {}
    for j in range(len(self.l)-1) :
      for i in range(len(self.l)-1) :
        if self.l[i][1] < self.l[i+1][1] :
          self.l[i] , self.l[i+1] = self.l[i+1] , self.l[i]
  def func(self) :
    for i in range(len(self.l)) :
      self.dic[self.l[i][0]] = self.l[i][1]
    return self.dic
obj = Db(l)
dic = obj.func()
print(dic,"\n\n\n")

#------------------------------------------------------------

# میانگین خطا ها را محاسبه میکنیم
sum = 0
for each_value in dic.values() :
  sum += each_value
print("average is",sum/5)
