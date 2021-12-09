import unittest
from practice import single_cart, credit_cart, timer_cart


class TestSingleMethod(unittest.TestCase) :
    def setUp(self) :
        self.cart = single_cart()

    def test_useble_cart(self) :
        self.assertTrue(self.cart.useable())
        self.assertFalse(self.cart.useable())


class TestCreditMethod(unittest.TestCase) :
    def setUp(self):
    	self.cart = credit_cart(money = 2000)
    
    def test_useble_cart(self) :
        self.assertTrue(self.cart.useable())
        self.assertTrue(self.cart.useable())
        self.assertFalse(self.cart.useable())

    def test_charge_money(self) :
        self.assertTrue(self.cart.charge_money(5000))
        self.assertFalse(self.cart.charge_money(500))


class TestTimerMethod(unittest.TestCase) :
    def setUp(self):
    	self.cart = timer_cart(money = 1000)
    
    def test_useble_cart(self) :
        self.assertTrue(self.cart.useable())
        self.assertFalse(self.cart.useable())

    def test_charge_money(self) :
        self.assertTrue(self.cart.charge_money(5000))
        self.assertFalse(self.cart.charge_money(500))

    def test_charge_time(self) :
        self.assertTrue(self.cart.charge_time())


unittest.main()