import random
from operator import itemgetter


class Immunity:
    def __init__(self, func, agents, clons, best, best_clon_numb, position_x, position_y):
        self.func = func

        self.pos_x = float(position_x)
        self.pos_y = float(position_y)

        self.agents_numb = agents
        self.agents = [[random.uniform(-self.pos_x, self.pos_x), random.uniform(-self.pos_y, self.pos_y), 0.0] for _ in
                       range(self.agents_numb)]

        for i in self.agents:
            i[2] = self.func(i[0], i[1])

        self.best = best
        self.best_clon_numb = best_clon_numb
        self.clon_numb = clons

    def immune_step(self, coef):

        best_pop = sorted(self.agents, key=itemgetter(2), reverse=False)[:self.best]

        new_pop = list()
        for pop in best_pop:
            for _ in range(self.clon_numb):
                new_pop.append(pop.copy())

        for npop in new_pop:
            npop[0] = npop[0] + coef * random.uniform(-0.5, 0.5)
            npop[1] = npop[1] + coef * random.uniform(-0.5, 0.5)
            npop[2] = self.func(npop[0], npop[1])

        new_pop = sorted(new_pop, key=itemgetter(2), reverse=False)[:self.best_clon_numb]

        self.agents += new_pop
        self.agents = sorted(self.agents, key=itemgetter(2), reverse=False)[:self.agents_numb]

    def get_best(self):
        return self.agents[0]