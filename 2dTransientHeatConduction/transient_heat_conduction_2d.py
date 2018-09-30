import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def create_mesh(nx, ny):
    # create 2d array with zeros size nx x ny, +2 for boundary conditions
    mesh = np.zeros((nx+2, ny+2))
    return mesh


def add_initial_conditions(mesh, temperature):
    # add constant value as initial condition
    for i in range(1, len(mesh)-1):
        for j in range(1, len(mesh)-1):
            mesh[i][j] = temperature
    return mesh


def add_boundary_conditions(mesh, top, bottom_left_right, left, right_top, right_bottom, bottom_middle):
    # pass values to boundary layers
    for i in range(1, len(mesh)-1):
        mesh[0][i] = top
    for j in range(1, len(mesh)-1):
        mesh[len(mesh)-1][j] = bottom_left_right
    for k in range(1, len(mesh)-1):
        mesh[k][0] = left
    for l in range(1, int(len(mesh)/2)):
        mesh[l][len(mesh)-1] = right_top
    for m in range(int(len(mesh)/2), len(mesh)-1):
        mesh[m][len(mesh) - 1] = right_bottom
    for n in range(4, 7):
        mesh[len(mesh) - 1][n] = bottom_middle
    return mesh


def calculations(mesh, dt, dx, rho, lambda_ooeff, cp, time_steps):
    alpha = lambda_ooeff / (cp * rho)
    tau = alpha * dt / (dx * dx)
    current_time = 0
    temperature_old = mesh
    temperature_new = mesh.copy()
    results = []

    while time_steps != 0:
        results.append(temperature_new.copy()[1:11, 1:11])

        for i in range(1, len(mesh)-1):
            for j in range(1, len(mesh)-1):
                temperature_new[i][j] = tau * (temperature_old[i-1][j] + temperature_old[i+1][j] + temperature_old[i][j-1]
                                               + temperature_old[i][j+1] - 4*temperature_old[i][j]) + temperature_old[i][j]

        temperature_old = temperature_new.copy()
        current_time += dt
        time_steps -= 1

    return results


def visualise_results(results):
    #plt.imshow(results[9], cmap='jet', interpolation='bicubic')
    #plt.axis('off')
    #plt.colorbar().set_label(u'\N{DEGREE SIGN}' + 'C', rotation=0, fontsize=15, labelpad=10)
    fig = plt.figure()
    list = []
    dt = 0
    for i in range(0, 1000):
        im = plt.imshow(results[i], cmap='jet', interpolation='bicubic', animated=True)
        list.append([im])
    plt.axis('off')
    plt.colorbar().set_label(u'\N{DEGREE SIGN}' + 'C', rotation=0, fontsize=15, labelpad=10)
    ani = animation.ArtistAnimation(fig, list, interval=50, blit=True,
                                    repeat_delay=1000)
    ani.save("transient_heat_conduction_2d.mp4")
    plt.show()

if __name__ == "__main__":
    mesh = create_mesh(10, 10)
    mesh = add_initial_conditions(mesh, 273)
    mesh = add_boundary_conditions(mesh, 373, 293, 288, 350, 320, 373)
    results = calculations(mesh, 0.1, 0.01, 2712, 237, 1507, 1001)
    visualise_results(results)