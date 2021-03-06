import unittest

from src.pub import Pub 
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Bill", 50)
   
    def test_can_decrease_wallet(self):
        drink = Drink("Beer", 3)
        self.customer.decrease_wallet(drink)
        self.assertEqual(47, self.customer.wallet)

    def test_add_drink_to_customer(self):
        drink = Drink("Beer", 3)
        self.customer.add_drink_to_customer(drink)
        self.assertEqual(1, len(self.customer.drinks))    