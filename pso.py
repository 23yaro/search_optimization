import random
import numpy as np
from operator import itemgetter


class PSO:
    def __init__(self, func, population, position_x, position_y, fi_p, fi_g):
        self.func = func
        self.population = population

        self.pos_x = float(position_x)
        self.pos_y = float(position_y)

        assert fi_p + fi_g > 4, "Сумма коэффициентов должна быть > 4"
        self.fi_p = fi_p
        self.fi_g = fi_g
        self.xi = 2 / (np.abs(2 - (fi_p + fi_g) - np.sqrt((fi_p + fi_g) ** 2 - 4 * (fi_p + fi_g))))

        self.particles = [[random.uniform(-self.pos_x, self.pos_x), random.uniform(-self.pos_y, self.pos_y), 0.0]
                          for _ in range(self.population)]
        for i in self.particles:
            i[2] = self.func(i[0], i[1])

        self.nostalgia = self.particles.copy()

        self.velocity = [[0.0 for _ in range(2)] for _ in range(self.population)]
        self.generation_best = min(self.particles, key=itemgetter(2))

    def update_velocity(self, velocity, particle, point_best) -> list:
        new_vel = list()
        for i in range(2):
            r1 = random.random()
            r2 = random.random()

            new_vel.append(self.xi * (velocity[i] + self.fi_p * r1 * (point_best[i] - particle[i]) + self.fi_g * r2 * (
                    self.generation_best[i] - particle[i])))
        return new_vel

    def update_position(self, velocity, particle):
        x = particle[0] + velocity[0]
        y = particle[1] + velocity[1]

        return [x, y, self.func(x, y)]

    def next_iteration(self):
        for i in range(self.population):

            if self.nostalgia[i][2] < self.particles[i][2]:
                point_best = self.nostalgia[i]
            else:
                self.nostalgia[i] = self.particles[i]
                point_best = self.particles[i]

            self.velocity[i] = PSO.update_velocity(self, self.velocity[i], self.particles[i], point_best)
            self.particles[i] = PSO.update_position(self, self.velocity[i], self.particles[i])

        self.generation_best = min(self.particles, key=itemgetter(2))