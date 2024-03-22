import numpy as np


def rosenbrock(x):
    return np.sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0, axis=0)


def rosenbrock_2(x, y):
    return (1.0 - x) ** 2 + 100.0 * (y - x * x) ** 2


def make_data_lab_3():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)

    x_grid, y_grid = np.meshgrid(x, y)

    z = rosenbrock(np.array([x_grid, y_grid]))
    return x_grid, y_grid, z
