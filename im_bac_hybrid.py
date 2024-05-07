import random
from operator import itemgetter


class ImmuBac:
    def __init__(self, func, agents, clons, best, best_clon_numb, chemostep, licvidation, position_x, position_y):
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

        self.chemo_step = chemostep
        self.licvid = licvidation

    def chemotaxis(func, step, populaton, coef):
        for bac in populaton:
            vec = [coef * random.uniform(-1, 1), coef * random.uniform(-1, 1)]
            for _ in range(step):
                f = bac[2]

                bac[0] += vec[0]  # X
                bac[1] += vec[1]  # Y
                bac[2] = func(bac[0], bac[1])  # Z / Фитнес-Функция

                if f < bac[2]:
                    vec = [coef * random.uniform(-1, 1), coef * random.uniform(-1, 1)]

        return populaton

    def elimnination(func, licvid, population, pos_x, pos_y):
        for bac in population:
            if random.uniform(0, 1) <= licvid:
                bac[0] = random.uniform(-pos_x, pos_x)
                bac[1] = random.uniform(-pos_y, pos_y)
                bac[2] = func(bac[0], bac[1])
        return population

    def immune_bact_step(self, coef):

        best_pop = sorted(self.agents, key=itemgetter(2), reverse=False)[:self.best]

        new_pop = list()
        for pop in best_pop:
            for _ in range(self.clon_numb):
                new_pop.append(pop.copy())

        new_pop = sorted(new_pop, key=itemgetter(2), reverse=False)[:self.best_clon_numb]

        self.agents += new_pop
        self.agents = ImmuBac.chemotaxis(self.func, self.chemo_step, self.agents, coef).copy()
        self.agents = ImmuBac.elimnination(self.func, self.licvid, self.agents, self.pos_x, self.pos_y).copy()
        self.agents = sorted(self.agents, key=itemgetter(2), reverse=False)[:self.agents_numb]

    def get_best(self):
        return self.agents[0]