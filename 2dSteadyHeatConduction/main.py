import numpy as np
import matplotlib.pyplot as plt
'''
2d steady heat equation with format nxn
Created by Sebastian Pajak
'''


class Calculations(object):

    def __init__(self, nx, ny):
        # mesh size
        self.nx, self.ny = nx, ny
        self.array = np.zeros((self.nx, self.ny))

    def add_boundary_conditions(self, x_top, x_bottom, y_left, y_right, corners):
        # set corners
        self.array[0][0] = corners[0]
        self.array[0][self.nx-1] = corners[1]
        self.array[self.ny-1][0] = corners[2]
        self.array[self.ny-1][self.nx-1] = corners[3]

        # add boundaries to wall
        for i in range(1, self.nx-1):
            self.array[0, i] = x_top
        for j in range(1, self.nx-1):
            self.array[self.nx-1, j] = x_bottom
        for k in range(1, self.ny-1):
            self.array[k, 0] = y_left
        for l in range(1, self.ny-1):
            self.array[l, self.nx-1] = y_right

    def calculate_temperature(self):

        # number of iterations
        iterations = 200

        for iter in range(1, iterations+1):
            for i in range(1, self.nx-1):
                for j in range(1, self.ny-1):
                    self.array[i][j] = (self.array[i-1][j] + self.array[i+1][j] + self.array[i][j-1] + self.array[i][j+1]) / 4

        plt.imshow(self.array, cmap='jet', interpolation='bicubic')
        plt.axis('off')
        plt.colorbar().set_label(u'\N{DEGREE SIGN}'+'C', rotation=0, fontsize=15, labelpad=10)
        plt.savefig('colormap.png')
        plt.show()


if __name__ == "__main__":
    calc = Calculations(18, 18)
    calc.add_boundary_conditions(0, 0, 20, 40, [0, 40, 5, 40])
    calc.calculate_temperature()