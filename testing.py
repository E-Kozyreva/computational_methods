from multiprocessing import Process
import matplotlib.pyplot as plt
import numpy as np

from alogithms.matrix_sugar import MatrixSugar as ms
from alogithms.hungarian import Hungarian as hg
from alogithms.greedy import Greedy as gr
from alogithms.saving import Saving as sv


class Testing(object):
    
    def __init__(self, size, min_start_sugar, max_start_sugar, min_degradation, max_degradation):
        self.size: int = size
        self.min_start_sugar: float = min_start_sugar
        self.max_start_sugar: float = max_start_sugar
        self.min_degradation: float = min_degradation
        self.max_degradation: float = max_degradation


    def create_matrix(self, has_breaking: bool) -> list:
        return ms(size=self.size, min_start_sugar=self.min_start_sugar,
                  max_start_sugar=self.max_start_sugar, min_degradation=self.min_degradation,
                  max_degradation=self.max_degradation, has_breaking=has_breaking).get_p_matrix()


    def test_hungarian(self) -> None:
        pt = self.create_matrix(has_breaking=True)

        h = hg(pt)
        res, indices = h._min()
        res, indices = h._max()

        pf = self.create_matrix(has_breaking=False)

        h = hg(pf)
        res, indices = h._min()
        res, indices = h._max()


    def test_greedy(self) -> None:
        pt = self.create_matrix(has_breaking=True)

        g = gr(p_matrix=pt, steps=1)
        res, indices = g.greedy()
        res, indices = g.greedy_saving()

        pf = self.create_matrix(has_breaking=False)

        g = gr(p_matrix=pf, steps=1)
        res, indices = g.greedy()
        res, indices = g.greedy_saving()

    
    def test_saving(self) -> None:
        pt = self.create_matrix(has_breaking=True)

        s = sv(p_matrix=pt, steps=1)
        res, indices = s.saving()
        res, indices = s.saving_greedy()

        pf = self.create_matrix(has_breaking=False)

        s = sv(p_matrix=pf, steps=1)
        res, indices = s.saving()
        res, indices = s.saving_greedy()

    
    def test_all(self) -> None:
        p1 = Process(target=self.test_hungarian, daemon=True)
        p2 = Process(target=self.test_greedy, daemon=True)
        p3 = Process(target=self.test_saving, daemon=True)
        p = [p1, p2, p3]
        for i in p:
            i.start()
        for i in p:
            i.join()


if __name__ == '__main__':
    path = ["time/hungarian_min.txt", "time/hungarian_max.txt", 
            "time/greedy.txt", "time/saving.txt",
            "time/greedy_saving.txt", "time/saving_greedy.txt"]
    
    for i in path:
        wf = open(i, "w")
        wf.close()

    for i in range(1, 100):
        t = Testing(size=i, min_start_sugar=1, max_start_sugar=1, min_degradation=0.7, max_degradation=0.7)
        t.test_all()

    x = np.arange(1, 199)
    y1 = np.loadtxt("time/hungarian_min.txt")
    y2 = np.loadtxt("time/hungarian_max.txt")
    y3 = np.loadtxt("time/greedy.txt")
    y4 = np.loadtxt("time/saving.txt")
    y5 = np.loadtxt("time/greedy_saving.txt")
    y6 = np.loadtxt("time/saving_greedy.txt")

    plt.plot(x, y1, label="hungarian_min")
    plt.plot(x, y2, label="hungarian_max")
    plt.plot(x, y3, label="greedy")
    plt.plot(x, y4, label="saving")
    plt.plot(x, y5, label="greedy_saving")
    plt.plot(x, y6, label="saving_greedy")
    plt.xlabel("size")
    plt.ylabel("time")
    plt.legend()
    plt.show()
