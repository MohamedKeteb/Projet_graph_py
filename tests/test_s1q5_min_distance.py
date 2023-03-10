# À compléter
import sys
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network00(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.get_path_min_dist(1, 4, 11)[1], 3)
        self.assertEqual(g.get_path_min_dist(2, 4, 10)[1], 2)

    def test_network04(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.get_path_min_dist(1, 4, 11)[1], 6)
        self.assertEqual(g.get_path_min_dist(1, 4, 11)[0], [1, 4])
        

if __name__ == '__main__':
    unittest.main()
