import numpy as np
import numdifftools as nd
from numpy import meshgrid, arange


def function(x, y):
    return x ** 2.0 + y ** 2.0


def make_data_lab_1():
    # define range for input
    r_min, r_max = -5.0, 5.0
    # sample input range uniformly at 0.1 increments
    x_axis = arange(r_min, r_max, 0.1)
    y_axis = arange(r_min, r_max, 0.1)
    # create a mesh from the axis
    x, y = meshgrid(x_axis, y_axis)
    # compute targets
    z = function(x, y)
    return x, y, z


def funct_consider(res_x, res_y, res_step, res_iterations):
    x_list = []
    y_list = []
    z_list = []

    # grid
    for item in gradient_descent(function, res_x, res_y, res_step, res_iterations):
        x_list.append(item[0])
        y_list.append(item[1])
        z_list.append(item[3])

    return x_list, y_list, z_list


def partial_function(f___, _input, pos, value):
    tmp = _input[pos]
    _input[pos] = value
    ret = f___(*_input)
    _input[pos] = tmp
    return ret


def gradient(fun, _input):
    ret = np.empty(len(_input))
    for i in range(len(_input)):
        def f_g(x): return partial_function(fun, _input, i, x)

        ret[i] = nd.Derivative(f_g)(_input[i])
    return ret


def next_point(x, y, gx, gy, step) -> tuple:
    return x - step * gx, y - step * gy


def gradient_descent(fun, x0, y0, tk, m):
    yield x0, y0, 0, fun(x0, y0)

    e1 = 0.0001
    e2 = 0.0001

    k = 0
    while True:
        (gx, gy) = gradient(fun, [x0, y0])  # 3

        if np.linalg.norm((gx, gy)) < e1:
            break

        if k >= m:  # Шаг 5
            break

        x1, y1 = next_point(x0, y0, gx, gy, tk)  # 7
        f1 = fun(x1, y1)
        f0 = fun(x0, y0)
        while not f1 < f0:
            tk = tk / 2
            x1, y1 = next_point(x0, y0, gx, gy, tk)
            f1 = fun(x1, y1)
            f0 = fun(x0, y0)

        if np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2) < e2 and abs(f1 - f0) < e2:  # 9
            break
        else:
            k += 1
            x0, y0 = x1, y1
            yield x0, y0, k, f1
