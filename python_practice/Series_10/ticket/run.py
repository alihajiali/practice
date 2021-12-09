import practice as p
from datetime import datetime


check = True
while check == True :
    work = input("what do you want ? \nregister - Authentication - log in - recovery password - exit \n")
    

    if work == "register" :
        full_name = input('please enter your full name : ')
        email = input('please enter your email : ')
        age = input('please enter your age : ')
        username = input('please enter your username : ')
        password = input('please enter your password : ')
        again_password = input('please enter your password agein : ')
        role = input('please enter your role : ')

        def register_work():
            is_check = client.check_person()
            if is_check == True:
                client.save2db()
                client.post_mail()
            else :
                print("i cann't register you :(")

        if role == 'admin':
            client = p.admin(full_name, email, age, username, password, again_password, role)
            register_work()
        elif role == 'employee':
            client = p.employee(full_name, email, age, username, password, again_password, role)
            register_work()
        elif role == 'student':
            client = p.student(full_name, email, age, username, password, again_password, role)
            register_work()
        elif role == 'person':
            client = p.person(full_name, email, age, username, password, again_password, role)
            register_work()
        else :
            print("this role is not avalibale :( ")
        
        print('\n'+'-'*38+'\n')


    elif work == "Authentication":
        code = input("please enter your code : ")
        client.check_code(code)

        print('\n'+'-'*38+'\n')


    elif work == "log in" :
        username = input('please enter your username : ')
        password = input('please enter your password : ')
        log_in = p.log_in(username, password)
        check_login = log_in.check()


        if check_login == True :
            while check_login == True :
                work2 = input("what do you want ? \nchange password - record - see - buy - manage - exit \n")


                if work2 == "change password":
                    password = input("please enter your password : ")
                    new_password = input("please enter your new password : ")
                    again_new_password = input("please enter your again new password : ")
                    change = p.change_password(username, password, new_password, again_new_password)
                    change.check_info()

                    print('\n'+'-'*38+'\n')


                elif work2 == "record":
                    type_record = input("what do you want ? \nAdvertising - discount \n")
                    
                    if type_record == "Advertising":
                        date = str(input('Enter date on this format : (y-m-d H:M:S): \n'))
                        place = input("please enter your place : ")
                        capacity = int(input("please enter your capacity : "))
                        money = int(input("please enter your money : "))
                        id_record = input('please enter id record : ')
                        record = p.record(date, username, place, capacity, money, id_record)
                        is_True = record.ckeck_info()
                        if is_True == True :
                            record.save2db()

                        print('\n'+'-'*38+'\n')

                    elif type_record == "discount":
                        date = str(input('Enter date on this format : (y-m-d H:M:S): \n'))
                        name = input("please enter name of this discount : ")
                        use_role = input("please enter use role : ")
                        discount = p.discount(username, name, date, use_role)
                        discount.save2db()

                        print('\n'+'-'*38+'\n')

                    else :
                        print("this record is invalid")

                        print('\n'+'-'*38+'\n')


                elif work2 == "manage":
                    id = input("what is your id record : ")
                    manage = p.manage(username)
                    manage.show_info(id)


                elif work2 == "see":
                    type_record = input("what do you want ? \nAdvertising - discount \n")
                    
                    if type_record == "Advertising":
                        see = p.see()
                        print('\n'+'='*38+'\n')
                        see.show()

                        print('\n'+'-'*38+'\n')

                    elif type_record == "discount":
                        see_discount = p.see_discount()
                        print('\n'+'='*38+'\n')
                        see_discount.show_discount()

                        print('\n'+'-'*38+'\n')

                    else :
                        print("this record is invalid")

                        print('\n'+'-'*38+'\n')


                elif work2 == "buy" :
                    buy = p.buy(username)

                    is_check = True
                    while is_check == True :
                        type_buy = input("what do you want ? \nadd advertising - add discount - invoice - pay - exit \n")

                        if type_buy == "add advertising" :
                            id_record = input("please enter id record : ")
                            number = int(input("please enter number : "))
                            buy.add_advertising(id_record, number)
                            
                        elif type_buy == "add discount" :
                            id_discount = input("please enter id discount :")
                            buy.add_discount(id_discount)

                        elif type_buy == "invoice" :
                            buy.invoice()

                        elif type_buy == "pay" :
                            result = input("hat do you want ? \npay->True - cancle->False \n")
                            buy.pay(result)

                        elif type_buy == "exit" :
                            is_check = False

                        else :
                            print("sorry your keyword is wrong :(")

                        print('\n'+'-'*38+'\n')


                elif work2 == "exit" :
                    check_login = False

                    print('\n'+'-'*38+'\n')


                else :
                    print("sorry your keyword is wrong :(")

                    print('\n'+'-'*38+'\n')


        else :
            print("sorry you isn't log in :(")

            print('\n'+'-'*38+'\n')


    elif work == "recovery password" :
        username = input("please enter your 'username' for recovery password : ")
        email = input("please enter your 'email' for recovery password : ")
        recovery = p.recovery_password(username, email)
        is_true = recovery.check_info()
        if is_true == True:
            recovery.post_mail()

        print('\n'+'-'*38+'\n')


    elif work == "exit" :
        check = False
        print("goodbye :) ")

        print('\n'+'-'*38+'\n')


    else :
        print("this keyword is wrong :(")

        print('\n'+'-'*38+'\n')

