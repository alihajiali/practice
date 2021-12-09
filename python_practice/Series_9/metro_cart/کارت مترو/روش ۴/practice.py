from datetime import datetime , timedelta

# cart class
class cart :
    """
    this is a parent class
    this class name is cart
    this class have a class variable (rent = 1000)
    rent is travel costs
    and this class have a property that is money (for first money every cart)
    """
    rent = 1000
    def __init__(self, money=0) :
        self.money = money

# this cart can use just once
class single_cart(cart) :
    """
    this class is child of class cart
    this class is for single cart (means use just once)
    this class have a method (usable) for use this cart
    you can not use more than once of this cart
    else you see this massage :
    'your cart is invalid :('
    """
    def __init__(self) :
        self.check = True
        
    def useable(self) :
        if self.check == True :
            self.check = False
            print('have a good trip :)')
        else :
            print('your cart is invalid :(')



# this cart can charge money
class credit_cart(cart) :
    """
    this class is child of class cart
    this class is for credit cart
    if money is enough you can use
    else you see this massage :
    your money isn't enough :(
    """
    def __init__(self, money) :
        super().__init__(money)

    def useable(self) :
        if self.money >= cart.rent :
            self.money -= cart.rent
            print('have a good trip :)')
        else :
            print("your money isn't enough :(")
        print(f'Your cart balance is : "{self.money}"')

    def charge_money(self, new_money) :
        if new_money > cart.rent :
            self.new_money = new_money
            self.money += self.new_money
            print(f'your money is : "{self.money}"')
        else :
            print('Your money is less than the minimum "less than the rent" :(')



# this cart can charge money & time
class timer_cart(cart) :
    """
    this class is child of class cart
    this class is for timer cart
    if money is enough you can use
    else you see this massage :
    your money isn't enough :(
    if time is avalible you can use
    else you see this massage :
    your cart is invalid :(
    """
    def __init__(self, money):
        super().__init__(money)
        self.time_limit = datetime.now()+timedelta(days=30)

    def useable(self) :
        time_use = datetime.now()
        if self.time_limit > time_use :
            if self.money >= cart.rent :
                self.money -= cart.rent
                print('have a good trip :)')
            else :
                print("your money isn't enough :(")
        else :
            print('your cart is invalid :(')
        print(f'Your cart balance is : "{self.money}"')
        print(f'Your cart time limit is : "{self.time_limit}"')

    def charge_money(self, new_money) :
        if new_money > cart.rent :
            self.new_money = new_money
            self.money += self.new_money
            print(f'your money is : "{self.money}"')
        else :
            print('Your money is less than the minimum "less than the rent" :(')

    def charge_time(self) :
        self.time_limit += timedelta(days = 30)
        print(f'your time limit is : "{self.time_limit}"')

#--------------------------------------------------------        

# objects

cart1 = single_cart()

cart2 = credit_cart(3000)

cart3 = timer_cart(2000)

#--------------------------------------------------------

cart1.useable()
cart2.useable()
cart3.useable()
cart2.charge_money(10000)
cart3.charge_money(10000)
cart3.charge_time()
cart1.useable()
cart2.useable()
cart3.useable()
print(cart.__doc__)