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
        wfile = open("time/hungarian_min_true.txt", "a")
        wfile.write(f"{sum(res)}\n")
        wfile.close()

        res, indices = h._max()
        wfile = open("time/hungarian_max_true.txt", "a")
        wfile.write(f"{sum(res)}\n")
        wfile.close()

        pf = self.create_matrix(has_breaking=False)

        h = hg(pf)
        res, indices = h._min()
        wfile = open("time/hungarian_min_false.txt", "a")
        wfile.write(f"{sum(res)}\n")
        wfile.close()
        res, indices = h._max()
        wfile = open("time/hungarian_max_false.txt", "a")
        wfile.write(f"{sum(res)}\n")
        wfile.close()


    def test_greedy(self) -> None:
        pt = self.create_matrix(has_breaking=True)

        g = gr(p_matrix=pt, steps=1)
        res, indices = g.greedy()
        wfile = open("time/greedy_true.txt", "a")
        wfile.write(f"{res}\n")
        wfile.close()
        res, indices = g.greedy_saving()
        wfile = open("time/greedy_saving_true.txt", "a")
        wfile.write(f"{res}\n")
        wfile.close()

        pf = self.create_matrix(has_breaking=False)

        g = gr(p_matrix=pf, steps=1)
        res, indices = g.greedy()
        wfile = open("time/greedy_false.txt", "a")
        wfile.write(f"{res}\n")
        wfile.close()
        res, indices = g.greedy_saving()
        wfile = open("time/greedy_saving_false.txt", "a")
        wfile.write(f"{res}\n")
        wfile.close()

    
    def test_saving(self) -> None:
        pt = self.create_matrix(has_breaking=True)

        s = sv(p_matrix=pt, steps=1)
        res, indices = s.saving()
        wfile = open("time/saving_true.txt", "a")
        wfile.write(f"{res}\n")
        wfile.close()
        res, indices = s.saving_greedy()
        wfile = open("time/saving_greedy_true.txt", "a")
        wfile.write(f"{res}\n")
        wfile.close()

        pf = self.create_matrix(has_breaking=False)

        s = sv(p_matrix=pf, steps=1)
        res, indices = s.saving()
        wfile = open("time/saving_false.txt", "a")
        wfile.write(f"{res}\n")
        wfile.close()
        res, indices = s.saving_greedy()
        wfile = open("time/saving_greedy_false.txt", "a")
        wfile.write(f"{res}\n")
        wfile.close()

    
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
    
    path = ["time/hungarian_min_true.txt", "time/hungarian_max_true.txt", 
            "time/hungarian_min_false.txt", "time/hungarian_max_false.txt", 
            "time/greedy_true.txt", "time/greedy_false.txt", 
            "time/greedy_saving_true.txt", "time/greedy_saving_false.txt", 
            "time/saving_true.txt", "time/saving_false.txt", 
            "time/saving_greedy_true.txt", "time/saving_greedy_false.txt"]
    
    for i in path:
        wf = open(i, "w")
        wf.close()

    days = int(input("days: "))
    min_start_sugar = float(input("min_start_sugar: "))
    max_start_sugar = float(input("max_start_sugar: "))
    min_degradation = float(input("min_degradation: "))
    max_degradation = float(input("max_degradation: "))


    for i in range(1, days):
        t = Testing(size=i, 
                    min_start_sugar=min_start_sugar, 
                    max_start_sugar=max_start_sugar, 
                    min_degradation=min_degradation, 
                    max_degradation=max_degradation)
        t.test_all()

    x = np.arange(1, days)
    y1 = np.loadtxt("time/hungarian_min_true.txt")
    y2 = np.loadtxt("time/hungarian_max_true.txt")
    y3 = np.loadtxt("time/hungarian_min_false.txt")
    y4 = np.loadtxt("time/hungarian_max_false.txt")
    y5 = np.loadtxt("time/greedy_true.txt")
    y6 = np.loadtxt("time/greedy_false.txt")
    y7 = np.loadtxt("time/greedy_saving_true.txt")
    y8 = np.loadtxt("time/greedy_saving_false.txt")
    y9 = np.loadtxt("time/saving_true.txt")
    y10 = np.loadtxt("time/saving_false.txt")
    y11 = np.loadtxt("time/saving_greedy_true.txt")
    y12 = np.loadtxt("time/saving_greedy_false.txt")

    plt.plot(x, y3, label="hungarian_min_false")
    plt.plot(x, y4, label="hungarian_max_false")
    plt.plot(x, y6, label="greedy_false")
    plt.plot(x, y8, label="greedy_saving_false")
    plt.plot(x, y10, label="saving_false")
    plt.plot(x, y12, label="saving_greedy_false")
    plt.legend()
    plt.xlabel("size")
    plt.ylabel("time")
    plt.savefig("time/time.png")
