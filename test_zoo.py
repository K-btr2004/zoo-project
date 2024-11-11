import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.

    #Boundary Value Analysis
    def test_Invalid_age_BVA(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid input")

    def test_min_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(1), 50)

    def test_max_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
        self.assertEqual(self.zoo.get_ticket_price(11), 50)

    def test_min_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(14), 100)
   
    def test_max_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def test_min_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(22), 150)

    def test_max_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
        self.assertEqual(self.zoo.get_ticket_price(59), 150)

    def test_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    #Equivalent Claass Partitioning
    def test_Invalid_age_ECP(self):
        self.assertEqual(self.zoo.get_ticket_price(-2), "Invalid input")

    def test_teen_ticket_price_(self):
        self.assertEqual(self.zoo.get_ticket_price(18), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)

    def test_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

if __name__ == '__main__':
    unittest.main()