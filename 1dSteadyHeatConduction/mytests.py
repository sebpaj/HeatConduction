import unittest
from main import *

calc = Calculations(1, 10)


class Tests(unittest.TestCase):
    def test_mesh(self):
        self.assertEqual([x for x in calc.create_mesh()], [x for x in np.linspace(0, 0, 11)])

    def test_boundary_conditions(self):
        calc.create_mesh()
        self.assertAlmostEqual(calc.add_boundary(1000, 10, 0.22)[0], 454.545454, delta=0.000001)
        self.assertAlmostEqual(calc.add_boundary(1000, 10, 0.22)[10], 10, delta=0.000001)
