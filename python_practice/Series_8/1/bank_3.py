from datetime import datetime
import time

#-----------------------------------------------------------

class Bank :

    # حداقل موجودی در حساب باید ۱۰۰۰۰ تومان باشد
    minimal_money = 10000


    def __init__(self, name, money) :
        self.name = name
        self.money = money

        #برای هر صاحب حساب یک دیکشنری تعریف کردم تا تراکنش هایی که انجام میدهد را بصورت لیست ذخیره کنم
        globals()['lst_'+self.name] = []



    # متد زیر به موجودی یک حساب مقداری را اضافه میکند و برای رسید یک متن را چاپ میکند
    def add_money(self, add) :

        self.money += add
        print('Your transaction was successful !!!')
        print(f'cash of {self.name} : {self.money}')

        transaction = {}
        t = datetime.now()
        transaction['time'] = t.strftime('%Y/%m/%d - %H:%M:%S')
        transaction['action'] = f'deposit:{add} - cash:{self.money}'
        globals()['lst_'+self.name].append(transaction)



    # متد زیر به موجودی یک حساب مقداری را کم میکند و برای رسید یک متن را چاپ میکند
    def sub(self, sub) :

        self.money -= sub
        print(f'cash of {self.name} : {self.money}')
        transaction = {}
        t = datetime.now()
        transaction['time'] = t.strftime('%Y/%m/%d - %H:%M:%S')
        transaction['action'] = f'withdraw:{sub} - cash:{self.money}'
        globals()['lst_'+self.name].append(transaction)




    # متد خصوصی زیر چک میکند که موجودی حساب بعد از انجام تراکنش کمتر از حداقل موجودی نشود و پیغام مناسب چاپ میکند
    def __check(self, request) :

        if self.money-request >= Bank.minimal_money :
            print('Your transaction was successful !!!')
            return True

        else :
            print('Your inventory is not enough !!!')
            return False



    # متد زیر تراکنش را انجام میدهد
    def send_money(self, origin, request, goal) :

        if origin._Bank__check(request) == True :
            origin.sub(request)
            goal.add_money(request)

        else :
            transaction = {}
            t = datetime.now()
            transaction['time'] = t.strftime('%Y/%m/%d - %H:%M:%S')
            transaction['action'] = f'the transaction failed - cash:{self.money}'
            globals()['lst_'+self.name].append(transaction)



        # متد زیر از موجودی یک حساب مقداری را کم میکند و برای رسید یک متن را چاپ میکند
    def sub_money(self, person, sub) :

        if person._Bank__check(sub) == True :
            person.sub(sub)

        else :
            transaction = {}
            t = datetime.now()
            transaction['time'] = t.strftime('%Y/%m/%d - %H:%M:%S')
            transaction['action'] = f'the transaction failed - cash:{self.money}'
            globals()['lst_'+self.name].append(transaction)


#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------


    # متر زیر تراکنش ها را چاپ میکند
    def transaction(self) :

        for t in globals()['lst_'+self.name] :
            print(t)

#-----------------------------------------------------------

    # متد زیر تراکنش های ۲ دیقه قبل و بعد زمان ورودی را چاپ میکند
    def tow_min(self, user_time) :

        # تبدیل زمان ورودی کاربر به ایپاک
        user_time = time.mktime(user_time)
        start_time = user_time - 120
        start_time = datetime.fromtimestamp(start_time)
        stop_time = user_time + 120
        stop_time = datetime.fromtimestamp(stop_time)

        # یافتن لیست کاربر مورد نظر و پیمایش روی دیکشنری های ان
        for dic in globals()['lst_'+self.name] :
            # تبدیل کلید های دیکشنری به فرمت دیت تایم
            t = datetime.strptime(dic['time'], '%Y/%m/%d - %H:%M:%S')

            if t >= start_time and t <= stop_time :
                print(dic)



#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------



lst = []
person1 = Bank('ali', 100000)
person2 = Bank('reza', 200000)
person3 = Bank('ahmad', 300000)

#-----------------------------------------------------------
#-----------------------------------------------------------

per = 'again'

while per == 'again' :

    work = input('_'*80+''+'\n\nplease choose between  :\nadd money - sub money - send money - transaction - two min transaction - anything\n\n')
    print('_'*80+'\n')
    

    if work == 'any thing' :
        per = ''
        print('thank you')


    elif work == 'add money' :
        origin = input('Please specify the recipient : ')
        money = int(input('how much money ? '))
        print('\n')

        if origin == 'person1' :
            person1.add_money(money)

        elif origin == 'person2' :
            person2.add_money(money)

        elif origin == 'person3' :
            person3.add_money(money)
        
        else :
            print('person is wrong ... ')

        


    elif work == 'sub money' :
        goal = input('Please specify the recipient : ')
        money = int(input('how much money ? '))
        print('\n')

        if goal == 'person1' :
            person1.sub_money(person1, money)

        elif goal == 'person2' :
            person2.sub_money(person2, money)

        elif goal == 'person3' :
            person3.sub_money(person3, money)

        else :
            print('person is wrong ... ')
    

    elif work == 'send money' :
        origin = input('Please specify the recipient : ')
        money = int(input('how much money ? '))
        goal = input('Please specify the recipient : ')
        print('\n')

        if origin == 'person1' and goal == 'person2' :
            person1.send_money(person1, money, person2)

        elif origin == 'person1' and goal == 'person3' :
            person1.send_money(person1, money, person3)

        elif origin == 'person2' and goal == 'person1' :
            person2.send_money(person2, money, person1)

        elif origin == 'person2' and goal == 'person3' :
            person2.send_money(person2, money, person3)

        elif origin == 'person3' and goal == 'person1' :
            person3.send_money(person3, money, person1)

        elif origin == 'person3' and goal == 'person2' :
            person3.send_money(person3, money, person2)
        
        else :
            print('person is wrong ... ')


    elif work == 'transaction' :
        person = input('What transaction do you want : ')
        print('\n')

        if person == 'person1' :
            person1.transaction()

        elif person == 'person2' :
            person2.transaction()

        elif person == 'person3' :
            person3.transaction()

    
    elif work == 'two min transaction' :
        person = input('What transaction do you want : ')
        year = int(input('please enter your year : '))
        month = int(input('please enter your month : '))
        day = int(input('please enter your day : '))
        hour = int(input('please enter your hour : '))
        minute = int(input('please enter your minute : '))
        second = int(input('please enter your second : '))
        print('\n')

        if person == 'person1' :
            person1.tow_min((year, month, day, hour, minute, second, 0, 0, -1))

        elif person == 'person2' :
            person2.tow_min(year, month, day, hour, minute, second, 0, 0, 0, -1)

        elif person == 'person3' :
            person3.tow_min(year, month, day, hour, minute, second, 0, 0, 0, -1)

    
    else :
        print('_'*80+''+'\n\nplease choose between  :\nadd money - sub money - send money - transaction - two min transaction - anything\n\n'+'_'*80+'\n')