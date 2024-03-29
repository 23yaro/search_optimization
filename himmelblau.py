import numpy as np


def make_data_himmelblau(p_X, p_Y):
    x = np.linspace(-p_X, p_X, 100)
    y = np.linspace(-p_Y, p_Y, 100)

    x_grid, y_grid = np.meshgrid(x, y)

    z = himmelblau(np.array([x_grid, y_grid]))
    return x_grid, y_grid, z


def himmelblau(x):
    return np.sum(2 * x[:-1] ** 2 + 3 * x[1:] ** 2 + 4 * x[:-1] * x[1:] - 6 * x[:-1] - 3 * x[1:], axis=0)


def himmelblau_2(x, y):
    return 2 * x * x + 3 * y * y + 4 * x * y - 6 * x - 3 * y