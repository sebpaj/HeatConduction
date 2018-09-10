import unittest
from transient_heat_conduction_1d import *


class Tests(unittest.TestCase):
    def test_mesh_creation(self):
        self.assertEqual([x for x in create_mesh(12)], [x for x in np.linspace(0, 0, 12)])

    def test_add_initial_conditions(self):
        self.assertEqual([x for x in add_initial_conditions([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 373)],
                               [373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373])

    def test_add_convection(self):
        self.assertAlmostEqual(add_convection([373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373],
                                              401, 0.05, 278, 50)[11], 367.424882787841, delta=0.5)