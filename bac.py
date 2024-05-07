import random
from operator import itemgetter


class Bacteria:
    def __init__(self, func, population, chemotaxis, licvidation, position_x, position_y):
        self.func = func

        self.pos_x = float(position_x)
        self.pos_y = float(position_y)

        self.pop_numb = int(population)
        self.agents = [[random.uniform(-self.pos_x, self.pos_x), random.uniform(-self.pos_y, self.pos_y), 0.0, 0.0] for
                       _ in
                       range(self.pop_numb)]

        for i in self.agents:
            i[2] = self.func(i[0], i[1])
            i[3] = i[2]

        self.chemo_step = chemotaxis
        self.licvid = licvidation

    def chemotaxis(self, coef):
        for bac in self.agents:
            vec = [coef * random.uniform(-1, 1), coef * random.uniform(-1, 1)]
            for _ in range(self.chemo_step):
                f = bac[2]

                bac[0] += vec[0]  # X
                bac[1] += vec[1]  # Y
                bac[2] = self.func(bac[0], bac[1])  # Z / Фитнес-Функция
                bac[3] += bac[2]  # Health

                if f < bac[2]:
                    vec = [coef * random.uniform(-1, 1), coef * random.uniform(-1, 1)]

    def reproduction(self):
        self.agents = sorted(self.agents, key=itemgetter(3), reverse=False)
        for i in range(self.pop_numb // 2):
            self.agents[self.pop_numb // 2 + i] = self.agents[i].copy()

    def elimnination(self):
        for bac in self.agents:
            if random.uniform(0, 1) <= self.licvid:
                bac[0] = random.uniform(-self.pos_x, self.pos_x)
                bac[1] = random.uniform(-self.pos_y, self.pos_y)
                bac[2] = self.func(bac[0], bac[1])
                bac[3] = bac[2]

    def get_best(self):
        return sorted(self.agents, key=itemgetter(2), reverse=False)[0]