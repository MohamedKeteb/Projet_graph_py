import sys 
sys.path.append("delivery_network")

import unittest
from graph import trucks_filter

class Test_trucks_filter(unittest.TestCase):
    def test_trucks1(self):
        T=trucks_filter("input/trucks.1.in")
        self.assertEqual((1000000,00000) in T,True)

    def test_trucks1(self):
        T=trucks_filter("input/trucks.0.in")
        self.assertEqual(len(T),2)

    def test_trucks1(self):
        T=trucks_filter("input/trucks.0.in")
        self.assertEqual((175000,17267) in T,False)

    
if __name__ == '__main__':
    unittest.main()