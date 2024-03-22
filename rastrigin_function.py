import numpy as np


def make_data_rastrigin(p_X, p_Y):
    x = np.linspace(-p_X, p_X, 100)
    y = np.linspace(-p_Y, p_Y, 100)

    x_grid, y_grid = np.meshgrid(x, y)

    z = rastrigin(np.array([x_grid, y_grid]))
    return x_grid, y_grid, z


def rastrigin(x):
    return np.sum(x[1:] ** 2 - 10 * np.cos(2 * np.pi * x[1:]) + x[:-1] ** 2 - 10 * np.cos(2 * np.pi * x[:-1]), axis=0)


def rastrigin_2(x, y):
    return x ** 2 - 10 * np.cos(2 * np.pi * x) + y ** 2 - 10 * np.cos(2 * np.pi * y)
