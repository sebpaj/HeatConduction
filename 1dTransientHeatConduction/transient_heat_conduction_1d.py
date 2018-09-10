import numpy as np
import matplotlib.pyplot as plt
"""
1d transient heat conduction
Created by Sebastian Pajak
"""


def create_mesh(nodes):
    mesh = np.zeros(nodes)
    return mesh


def add_initial_conditions(mesh, temperature):
    for i in range(len(mesh)):
        mesh[i] = temperature
    return mesh


def add_convection(mesh, lambda_coeff, dx, T_inf, air_alpha):
    mesh[len(mesh)-1] = -(air_alpha*(mesh[len(mesh)-2]-T_inf)) * dx * (len(mesh)-2) / lambda_coeff + mesh[0]
    return mesh

def calculations(mesh, rho, lambda_coeff, Cp, dx, dt):
    iterations = 200
    time_step = 0
    alpha = lambda_coeff / (Cp*rho)
    tau = alpha*dt / (dx*dx)
    temp_old = mesh
    temp_new = mesh
    results = []
    for i in range(0, iterations+1):
        if time_step == 0 or time_step == 60 or time_step == 300 or time_step == 1800 or time_step == 10:
            results.append(temp_new.copy())

        for item in range(1, len(mesh)-1):
            temp_new[item] = tau*(temp_old[item-1] - 2 * temp_old[item] + temp_old[item+1]) + temp_old[item]
        temp_old = temp_new
        time_step += dt

    return results


def visualise_results(results):
    x_axis_value = np.linspace(0, 0.5, 11)
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(8, 6))
    fig.tight_layout()  # Or equivalently,  "plt.tight_layout()"
    plt.subplots_adjust(wspace=0.3, hspace=0.75)
    plt.subplots_adjust(left=0.1, bottom=0.10)

    # plot 0s
    plt.subplot(321)
    plt.plot(x_axis_value, results[0][:-1])
    plt.title('Time: 0s')
    plt.xlabel("Length [m]")
    plt.ylabel("Temperature: " + "[" + u"\N{DEGREE SIGN}" + "C]")
    plt.ylim(365, 375)
    # plot 10s
    plt.subplot(322)
    plt.plot(x_axis_value, results[1][:-1])
    plt.title('Time: 10s')
    plt.xlabel("Length [m]")
    plt.ylabel("Temperature: " + "[" + u"\N{DEGREE SIGN}" + "C]")
    plt.ylim(365, 375)
    # plot 60s
    plt.subplot(323)
    plt.plot(x_axis_value, results[2][:-1])
    plt.title('Time: 60s')
    plt.xlabel("Length [m]")
    plt.ylabel("Temperature: " + "[" + u"\N{DEGREE SIGN}" + "C]")
    plt.ylim(365, 375)
    # plot 300s
    plt.subplot(324)
    plt.plot(x_axis_value, results[3][:-1])
    plt.title('Time: 300s')
    plt.xlabel("Length [m]")
    plt.ylabel("Temperature: " + "[" + u"\N{DEGREE SIGN}" + "C]")
    plt.ylim(365, 375)
    # plot 1800s
    plt.subplot(325)
    plt.plot(x_axis_value, results[4][:-1])
    plt.title('Time: 1800s')
    plt.xlabel("Length [m]")
    plt.ylabel("Temperature: " + "[" + u"\N{DEGREE SIGN}" + "C]")
    plt.ylim(365, 375)

    plt.show()

if __name__ == "__main__":
    # mesh with 12 nodes
    mesh = create_mesh(12)
    # set 373 K temperature as initial temperature
    mesh = add_initial_conditions(mesh, 373)
    # add convection
    mesh = add_convection(mesh, 401, 0.05, 278, 50)
    # calculate
    results = calculations(mesh, 8960, 401, 384.4, 0.05, 10)
    # plotting data
    visualise_results(results)