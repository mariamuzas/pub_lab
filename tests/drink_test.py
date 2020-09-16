import unittest

from src.pub import Pub 
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def test_get_name(self):
        self.drink = Drink("Beer", 3.5)
        self.assertEqual("Beer", self.drink.name)