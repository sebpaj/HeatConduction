import numpy as np
import matplotlib.pyplot as plt

'''
1d stady heat equation with heat flux as left boundary condition
Created by Sebastian Pajak
'''


class Calculations(object):

    def __init__(self, wall_length, nodes):
        self.wall_length = wall_length
        self.nodes = nodes
        self.dx = wall_length / nodes
        self.mesh = None

    def create_mesh(self):
        # create 1d array
        self.mesh = np.linspace(0, 0, self.nodes + 1, endpoint=True)
        return self.mesh

    def add_boundary(self, heat_flux, temperature_boundary, material_conductivity):
        self.mesh[len(self.mesh)-1] = temperature_boundary
        self.mesh[0] = heat_flux * self.dx / material_conductivity
        return self.mesh

    def calculate_temperature(self, iterations):
        for iter in range(0, iterations+1):
            for i in range(1, self.nodes):
                self.mesh[i] = (self.mesh[i-1] + self.mesh[i+1]) / 2
        return self.mesh

    def visualise_results(self):
        nodes_array = np.linspace(0, self.wall_length, self.nodes+1, endpoint=True)
        plt.plot(nodes_array, self.mesh)
        plt.title('Heat conduction', fontsize=20)
        plt.xlabel('Length [m]')
        plt.ylabel('Temperature '+u'\N{DEGREE SIGN}'+'C')
        plt.savefig('1dheatconduction.png')
        plt.show()


if __name__ == "__main__":
    np.set_printoptions(linewidth=np.inf)
    calc = Calculations(1, 10)
    calc.create_mesh()
    calc.add_boundary(100, -10, 0.22)
    calc.calculate_temperature(20)
    calc.visualise_results()