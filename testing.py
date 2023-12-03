from alogithms.matrix_sugar import MatrixSugar as ms
from alogithms.hungarian import Hungarian as hung
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
        wfile = open("output/hungarian.txt", "w")
        pt = self.create_matrix(has_breaking=True)
        wfile.write(f"Matrix with has_breaking: True\n")
        for i in pt:
            wfile.write(f"{i}\n")

        h = hung(pt)
        res, indices = h._min()
        wfile.write(f"\nhungarian_min: {res}\n{indices}\n\n")

        res, indices = h._max()
        wfile.write(f"hungarian_max: {res}\n{indices}\n\n")

        pf = self.create_matrix(has_breaking=False)
        wfile.write(f"\nMatrix with has_breaking: False\n")
        for i in pf:
            wfile.write(f"{i}\n")

        h = hung(pf)
        res, indices = h._min()
        wfile.write(f"\nhungarian_min: {res}\n{indices}\n\n")

        res, indices = h._max()
        wfile.write(f"hungarian_max: {res}\n{indices}")
        wfile.close()


    def test_greedy(self) -> None:
        wfile = open("output/greedy.txt", "w")
        pt = self.create_matrix(has_breaking=True)
        wfile.write(f"Matrix with has_breaking: True\n")
        for i in pt:
            wfile.write(f"{i}\n")

        g = gr(p_matrix=pt, steps=1)
        res, indices = g.greedy()
        wfile.write(f"\ngreedy: {res}\n{indices}\n\n")

        res, indices = g.greedy_saving()
        wfile.write(f"greedy_saving: {res}\n{indices}\n\n")

        pf = self.create_matrix(has_breaking=False)
        wfile.write(f"\nMatrix with has_breaking: False\n")
        for i in pf:
            wfile.write(f"{i}\n")

        g = gr(p_matrix=pf, steps=1)
        res, indices = g.greedy()
        wfile.write(f"\ngreedy: {res}\n{indices}\n\n")

        res, indices = g.greedy_saving()
        wfile.write(f"greedy_saving: {res}\n{indices}")
        wfile.close()

    
    def test_saving(self) -> None:
        wfile = open("output/saving.txt", "w")
        pt = self.create_matrix(has_breaking=True)
        wfile.write(f"Matrix with has_breaking: True\n")
        for i in pt:
            wfile.write(f"{i}\n")

        s = sv(p_matrix=pt, steps=1)
        res, indices = s.saving()
        wfile.write(f"\nsaving: {res}\n{indices}\n\n")

        res, indices = s.saving_greedy()
        wfile.write(f"saving_greedy: {res}\n{indices}\n\n")

        pf = self.create_matrix(has_breaking=False)
        wfile.write(f"\nMatrix with has_breaking: False\n")
        for i in pf:
            wfile.write(f"{i}\n")

        s = sv(p_matrix=pf, steps=1)
        res, indices = s.saving()
        wfile.write(f"\nsaving: {res}\n{indices}\n\n")

        res, indices = s.saving_greedy()
        wfile.write(f"saving_greedy: {res}\n{indices}")
        wfile.close()

    
    def test_all(self) -> None:
        self.test_hungarian()
        self.test_greedy()
        self.test_saving()


if __name__ == '__main__':
    t = Testing(size=8, min_start_sugar=1, max_start_sugar=1, min_degradation=0.7, max_degradation=0.7)
    t.test_all()
