import pickle

class Bank :
    # حداقل موجودی در حساب باید ۱۰۰۰۰ تومان باشد
    minimal_money = 10000
    def __init__(self, name, money) :
        self.name = name
        self.money = money
        # یک دیکشنری برای هر شخص که حساب باز میکند ساختیم و اطلاعات ان شخص مثل نام و موجودی در ان ذخیره میشود
        self.detail = {}
        self.detail['name'] = self.name
        self.detail['money'] = self.money
        # یک لیست را بصورت گلوبال ایمپورت میکنیم
        global lst  
        # و هر دیکشنری را در لیست اضافه میکنیم (زیرا بعدا میخواهیم روی ایتم های لیست پیمایش کنیم)
        lst.append(self.detail) 
        # و لیست را داخل یک فایل پیکل مینویسیم
        with open('data.pickle', 'wb') as writer :
            pickle.dump(lst, writer)

    # متد زیر به موجودی یک حساب مقداری را اضافه میکند و برای رسید یک متن را چاپ میکند
    def add_money(self, add) :
        with open('data.pickle', 'rb') as reader :
            # فایل پیکل را میخواند و لیستی از کاربران را ایجاد میکند
            lst = pickle.load(reader)
            for person_goal in lst :
                if person_goal['name'] == self.name :
                    self.money += add
                    print(f'cash of {self.name} : {self.money}')
                    person_goal['money'] = self.money
        with open('data.pickle', 'wb') as writer :
            pickle.dump(lst, writer)

    # متد زیر از موجودی یک حساب مقداری را کم میکند و برای رسید یک متن را چاپ میکند
    def sub_money(self, sub) :
        with open('data.pickle', 'rb') as reader :
            # فایل پیکل را میخواند و لیستی از کاربران را ایجاد میکند
            lst = pickle.load(reader)
            for person_origin in lst :
                if person_origin['name'] == self.name :
                    self.money -= sub
                    print(f'cash of {self.name} : {self.money}')
                    person_origin['money'] = self.money
        with open('data.pickle', 'wb') as writer :
            pickle.dump(lst, writer)

    # متد خصوصی زیر چک میکند که موجودی حساب بعد از انجام تراکنش کمتر از حداقل موجودی نشود و پیغام مناسب چاپ میکند
    def __check(self, request) :
        with open('data.pickle', 'rb') as reader :
            for person_origin in pickle.load(reader) :
                if person_origin['name'] == self.name :
                    if person_origin['money']-request >= Bank.minimal_money :
                        print('Your transaction was successful !!!')
                        return True
                    else :
                        print('Your inventory is not enough !!!')
                        return False

    # متد زیر تراکنش را انجام میدهد
    def send_money(self, person1, request, person2) :
        if person1._Bank__check(request) == True :
            person1.sub_money(request)
            person2.add_money(request)
        
        
lst = []
person1 = Bank('ali', 50000)
person2 = Bank('reza', 10000)
person3 = Bank('ahmad', 20000)
person4 = Bank('hasan', 300000)
person5 = Bank('mohammad', 75000)
person6 = Bank('iman', 130000)
person7 = Bank('mahan', 900000)
print(person7.send_money(person7, 20000, person2))
