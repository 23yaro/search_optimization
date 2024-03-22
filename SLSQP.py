from scipy.optimize import minimize
import numpy as np
import numpy


def make_data_lab_2():
    x = numpy.linspace(-10, 10, 100)
    y = numpy.linspace(-10, 10, 100)

    x_grid, y_grid = numpy.meshgrid(x, y)

    z = 2 * x_grid * x_grid + 3 * y_grid * y_grid + 4 * x_grid * y_grid - 6 * x_grid - 3 * y_grid
    return x_grid, y_grid, z


def kp(x, y):
    # global points
    points = []

    # function
    def fun(x_i):
        x1 = x_i[0]
        x2 = x_i[1]
        return 2 * x1 * x1 + 3 * x2 * x2 + 4 * x1 * x2 - 6 * x1 - 3 * x2

    def callback(x_w):
        g_list = np.ndarray.tolist(x_w)
        g_list.append(fun(x_w))
        points.append(g_list)

    # searching range
    b = (0, float("inf"))
    bounds = (b, b)
    # initial point
    x0 = (x, y)
    con = {'type': 'eq', 'fun': fun}
    # main call
    res = minimize(fun, x0, method="SLSQP", bounds=bounds,
                   constraints=con, callback=callback)

    glist = np.ndarray.tolist(res.x)
    glist.append(res.fun)
    points.append(glist)

    for iteration, point in enumerate(points):
        yield iteration, point
