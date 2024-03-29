import random
from operator import itemgetter


class Bees:
    def __init__(self, func, scouts, elite, perspect, bees_to_leet, bees_to_persp, radius, position_x, position_y):
        self.func = func

        self.pos_x = float(position_x)
        self.pos_y = float(position_y)

        self.scouts = [[random.uniform(-self.pos_x, self.pos_x), random.uniform(-self.pos_y, self.pos_y), float(0.0)] for _ in
                       range(scouts)]

        for i in self.scouts:
            i[2] = self.func(i[0], i[1])

        self.n_workers = elite * bees_to_leet + perspect * bees_to_persp
        self.e = elite
        self.p = perspect
        self.b_leet = bees_to_leet
        self.b_persp = bees_to_persp

        max_b = max(self.scouts, key=itemgetter(2))
        self.workers = [[self.pos_x, self.pos_y, max_b[2]] for _ in range(self.n_workers)]

        self.bees = list()

        self.selected = list()

        self.rad = radius

    def send_scouts(self):
        for unit in self.scouts:
            unit[0] = random.uniform(-self.pos_x, self.pos_x)
            unit[1] = random.uniform(-self.pos_y, self.pos_y)
            unit[2] = self.func(unit[0], unit[1])

    def research_reports(self):
        self.bees = self.scouts + self.workers
        self.bees = sorted(self.bees, key=itemgetter(2), reverse=False)

        self.selected = self.bees[:self.e + self.p]

    def get_best(self):
        return self.bees[0]

    def send_workers(self, bee_part, sector, radius):
        for bee in bee_part:
            bee[0] = random.uniform(sector[0] - radius, sector[0] + radius)
            bee[1] = random.uniform(sector[1] - radius, sector[1] + radius)
            bee[2] = random.uniform(sector[2] - radius, sector[2] + radius)

    def selected_search(self, param):
        for i in range(self.e):
            Bees.send_workers(self.func, 
                              self.workers[i * self.b_leet:i * self.b_leet + self.b_leet],
                              self.selected[i],
                              self.rad * param)

        for i in range(self.p):
            Bees.send_workers(self.func, 
                              self.workers[self.e * self.b_leet + i * self.b_persp:self.e * self.b_leet +
                                                                                 i * self.b_persp + self.b_persp],
                              self.selected[self.e + i], 
                              self.rad * param)
