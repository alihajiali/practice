import redis
redisClient = redis.Redis()
import re
from random import randint
from datetime import datetime
import logging
from packages import send_mail


class client:
    def __init__(self, full_name, email, age, username, password, again_password, role):
        self.full_name = full_name
        self.email = email
        self.age = age
        self.username = username
        self.password = password
        self.again_password = again_password
        self.role = role
        
    def check_person(self):
        if redisClient.exists(f'user:{self.username}') == 0 :
            if re.search('^([\w\-\.]+)@([\w\-]+)\.([a-zA-Z]{2,5})$', self.email):
                if self.password == self.again_password:
                    if re.search('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$', self.password):
                        self.Authentication = str(randint(10000, 99999))
                        return True
                    else :
                        print("password is invalid")
                        return False
                else:
                    print("password and again_password isn't same :(")
                    return False
            else:
                print('your email is invalid :(')
                return False
        else :
            print('this username use before :(')
            return False

    def save2db(self):
        redisClient.hmset(
        f'user:{self.username}',
        {
        'full_name': self.full_name,
        'email': self.email,
        'age': self.age,
        'username': self.username,
        'password': self.password,
        'role': self.role
        }
        )

    def post_mail(self):
        redisClient.set(f"Authentication:{self.username}", self.Authentication)
        redisClient.expire(f"Authentication:{self.username}", 300)
        massage = f"your Authentication code is : {self.Authentication}"
        send_email = send_mail.mail(self.username, self.email, massage)
        send_email.send()
        print("please check your email and tell me your code :) ")

    def check_code(self, code):
        self.code = code
        if self.code == redisClient.get(f"Authentication:{self.username}").decode("utf-8") :
            redisClient.hset(f"user:{self.username}", "Authentication", "True")
            print("your register is Success")
        else :
            print('sorry ; your code is wrong :(')
        


class admin(client):
    discount = 40




class employee(client):
    discount = 30




class student(client):
    discount = 20




class person(client):
    discount = 10




class log_in:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check(self):
        if redisClient.hget(f"user:{self.username}", "Authentication").decode("utf-8") == "True" :
            if redisClient.hget(f'user:{self.username}', 'username').decode() == self.username:
                if redisClient.hget(f'user:{self.username}', 'password').decode() == self.password:
                    print("your log in is Success :)")
                    return True
        else :
            print("Your email has not yet been authenticated")
            return False



class recovery_password:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def check_info(self):
        if redisClient.exists(f'user:{self.username}') == 1:
            if redisClient.hget(f'user:{self.username}', 'email').decode() == self.email:
                self.password = redisClient.hget(f'user:{self.username}', 'password').decode()
                return True
            else :
                print("email is invalid :( ")
        else :
            print("this user is invalid")

    def post_mail(self):
        massage = f"your password is : {self.password}"
        send_email = send_mail.mail(self.username, self.email, massage)
        send_email.send()
        print("i send your password to your email :) ")


#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------

class change_password:
    def __init__(self, username, password, new_password, again_new_password):
        self.username = username
        self.password = password
        self.new_password = new_password
        self.again_new_password = again_new_password

    def check_info(self):
        if redisClient.hget(f'user:{self.username}', 'password').decode() == self.password:
            self.email = redisClient.hget(f'user:{self.username}', 'email').decode()
            if self.new_password == self.again_new_password:
                if re.search('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$', self.password):
                    redisClient.hset(f'user:{self.username}', 'password', self.new_password)
                    print("change your password is Success")
                else :
                    print("password is invalid")
            else :
                print("password and agein_password isn't same :(")
        else :
            print("password is invalid :( ")





class record:
    def __init__(self, date, username, place, capacity, money, id_record) :
        self.str_date = date
        self.date = datetime.strptime(self.str_date, "%Y-%m-%d %H:%M:%S")
        self.username = username
        self.place = place
        self.capacity = capacity
        self.remaining_capacity = self.capacity
        self.money = money
        self.id_record = id_record


    def ckeck_info(self):
        now_date = datetime.now()
        if redisClient.hget(f'user:{self.username}', "role").decode("utf-8") != "admin":
            print("you can not record (just admin can)")
            return False
        else :
            if now_date > self.date :
                print("your date is wrong :(")
                return False
            
            else :
                if self.capacity <= 0 :
                    print("your capacity is wrong :(")
                    return False
                else :
                    if self.money <= 0 :
                        print("your money is wrong :(")
                        return False
                    else :
                        return True


    def save2db(self):

        logging.basicConfig(level=logging.INFO, filename="msg.log")
        logging.info(f"make new record by name : record:{self.id_record}")

        redisClient.hmset(
        f"record:{self.id_record}",
        {
        'date': self.str_date,
        'place': self.place,
        'capacity': self.capacity,
        'username': self.username,
        'remaining_capacity': self.remaining_capacity,
        'money': self.money,
        }
        )
        redisClient.lpush("lst_of_record", f'record:{self.id_record}')
        print("your record is success :)")




class discount:
    def __init__(self, username, name, date, use_role):
        self.name = name
        self.username = username
        self.use_role = use_role
        self.str_date = date
        self.date = datetime.strptime(self.str_date, "%Y-%m-%d %H:%M:%S")

    def save2db(self):
        now_date = datetime.now()
        if redisClient.hget(f'user:{self.username}', "role").decode("utf-8") != "admin":
            print("you can not record (just admin can)")
            return False
        else :
            if now_date > self.date :
                print("your date is wrong :(")
                return False
            else:
                redisClient.hmset(
                f'discount:{self.name}',
                {
                'date': self.str_date,
                'username': self.username,
                'name': self.name,
                'use role' : self.use_role
                }
                )
                redisClient.lpush("lst_of_discount", f'discount:{self.name}')
                print("your discount is success :)")

                     

class see:
    def __init__(self):
        self.lst_of_record = redisClient.lrange('lst_of_record', 0, -1)
        self.time_now = datetime.now()

    def show(self):
        for record_name in self.lst_of_record:
            self.date = redisClient.hget(record_name.decode("utf-8"), "date").decode("utf-8")
            self.date = datetime.strptime(self.date, "%Y-%m-%d %H:%M:%S")
            if self.time_now < self.date:
                result_key = redisClient.hgetall(record_name.decode("utf-8"))
                print("record id : " + record_name.decode("utf-8"))
                print("date : " + result_key[b'date'].decode("utf-8"))
                print("place : " + result_key[b'place'].decode("utf-8"))
                print("capacity : " + result_key[b'capacity'].decode("utf-8"))
                print("remaining_capacity : " + result_key[b'remaining_capacity'].decode("utf-8"))
                print("money : " + result_key[b'money'].decode("utf-8"))

                print('\n'+'='*38+'\n')

            else:
                redisClient.lrem('lst_of_record', 1, record_name.decode("utf-8"))
                redisClient.delete(record_name.decode("utf-8"))



class see_discount:
    def __init__(self):
        self.lst_of_discount = redisClient.lrange('lst_of_discount', 0, -1)
        self.time_now = datetime.now()

    def show_discount(self):
        for discount_name in self.lst_of_discount:
            self.date = redisClient.hget(discount_name.decode("utf-8"), "date").decode("utf-8")
            self.date = datetime.strptime(self.date, "%Y-%m-%d %H:%M:%S")
            if self.time_now < self.date:
                result_key = redisClient.hgetall(discount_name.decode("utf-8"))
                print(discount_name.decode("utf-8"))
                print("date : " + result_key[b'date'].decode("utf-8"))
                print("name : " + result_key[b'name'].decode("utf-8"))
                print("use role : " + result_key[b'use role'].decode("utf-8"))

                print('\n'+'='*38+'\n')

            else:
                redisClient.lrem('lst_of_discount', 1, discount_name.decode("utf-8"))
                redisClient.delete(discount_name.decode("utf-8"))




class buy:
    def __init__(self, username):
        self.username = username

    def add_advertising(self, id_record, number):
        self.id_record = id_record
        self.number = number
        date = str(datetime.now())

        redisClient.hset(f'lst_shopping:{self.username}', "self.id_record", "self.number")
        if redisClient.hexists(f'lst_shopping:{self.username}', self.id_record) == 0:
            if int(redisClient.hget(self.id_record, 'remaining_capacity').decode("utf-8")) - self.number >= 0:
                redisClient.hset(f'lst_shopping:{self.username}', self.id_record, self.number)
                
                redisClient.hset(f'shopping:{self.username}', date, f"{self.id_record}")
                redisClient.hset(f'number_shopping:{self.username}', date, f"{self.number}")
                redisClient.lpush(f'lst_buy_of:{self.username}', date)
            
            else :
                print("Inventory is not enough")

        else:
            Demand = int(redisClient.hget(f'lst_shopping:{self.username}', self.id_record).decode("utf-8")) + self.number
            if Demand <= int(redisClient.hget(self.id_record, 'remaining_capacity').decode("utf-8")):
                redisClient.hset(f'lst_shopping:{self.username}', self.id_record, Demand)
            
                redisClient.hset(f'shopping:{self.username}', date, f"{self.id_record}")
                redisClient.hset(f'number_shopping:{self.username}', date, f"{self.number}")
                redisClient.lpush(f'lst_buy_of:{self.username}', date)

            else:
                print("Inventory is not enough")
    
    def add_discount(self, discount_name) :
        self.discount_name = discount_name
        self.type_user = redisClient.hget(f'user:{self.username}', 'role').decode("utf-8")
        self.type_discount = redisClient.hget(self.discount_name, 'use role').decode("utf-8")

        if self.type_user == self.type_discount :
            redisClient.set(f'discount_shopping:{self.username}', self.discount_name)

    def invoice(self):
        self.total_money = 0
        for each_buy in redisClient.lrange(f'lst_buy_of:{self.username}', 0, -1) :
            self.total_money += int(redisClient.hget(redisClient.hget(f'shopping:{self.username}', each_buy).decode("utf-8"), "money"))*int(redisClient.hget(f'number_shopping:{self.username}', each_buy).decode("utf-8"))
        print(f"total money : {self.total_money}")
        if redisClient.exists(f'discount_shopping:{self.username}') == 0 :
            print("discount : you don't have any discount :(")
            user_discount = 0
        else :
            self.type_user = redisClient.hget(f'user:{self.username}', 'role').decode("utf-8")
            
            if self.type_user == "admin" :
                user_discount = admin.discount

            elif self.type_user == "employee" :
                user_discount = employee.discount

            elif self.type_user == "student" :
                user_discount = student.discount

            elif self.type_user == "person" :
                user_discount = person.discount

            print(f"discount : {user_discount}%")

        amount_payable = self.total_money - (self.total_money/100*user_discount)
        print(f"amount payable is : {self.total_money} - {user_discount}% = {amount_payable}")


    def pay(self, result):
        self.result = result
        if self.result == 'False' :
            print("ok Thanks !")

        elif self.result == 'True' :

            for each_buy in redisClient.lrange(f'lst_buy_of:{self.username}', 0, -1) :
                each_record = redisClient.hget(f'shopping:{self.username}', each_buy).decode("utf-8")
                redisClient.hset(each_record, 'remaining_capacity', int(redisClient.hget(each_record, 'remaining_capacity').decode("utf-8"))-int(redisClient.hget(f'number_shopping:{self.username}', each_buy).decode("utf-8")))

            massage = f"you buy tiket ; goodluck"
            self.email = redisClient.hget(f"user:{self.username}", "email").decode("utf-8")
            send_email = send_mail.mail(self.username, self.email, massage)
            send_email.send()
            print("your tiket send to your email :)")

            lst1 = redisClient.hkeys(f"lst_shopping:{self.username}")
            for i in lst1:
                redisClient.hdel(f"lst_shopping:{self.username}", i)

            lst2 = redisClient.hkeys(f'shopping:{self.username}')
            for i in lst2:
                redisClient.hdel(f'shopping:{self.username}', i)

            lst3 = redisClient.hkeys(f'number_shopping:{self.username}')
            for i in lst3:
                redisClient.hdel(f'number_shopping:{self.username}', i)

            lst4 = redisClient.hkeys(f'discount_shopping:{self.username}')
            for i in lst4:
                redisClient.hdel(f'discount_shopping:{self.username}', i)

            lst = redisClient.lrange(f'lst_buy_of:{self.username}', 0, -1)
            for i in lst:
                redisClient.lrem(f'lst_buy_of:{self.username}', 0, i)

            


        else :
            print("this keywird is wrong")


class manage:
    def __init__(self, username):
        self.username = username

    def show_info(self, id_record):
        if redisClient.hget(f"user:{self.username}", "role").decode("utf-8") == "admin":
            self.id_record = id_record
            print(f"remaining capacity is : {redisClient.hget(self.id_record, 'remaining_capacity')} ticket")