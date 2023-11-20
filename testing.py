from alogithms.matrix_sugar import MatrixSugar as ms
from alogithms.hungarian import Hungarian as hung
from alogithms.greedy import Greedy as gr
from alogithms.saving import Saving as sv


if __name__ == '__main__':

    pt = ms(size=8, min_start_sugar=1, max_start_sugar=1,
           min_degradation=0.7, max_degradation=0.7, has_breaking=True).get_p_matrix()
    
    pf = ms(size=8, min_start_sugar=1, max_start_sugar=1,
            min_degradation=0.7, max_degradation=0.7, has_breaking=False).get_p_matrix()


    # Венгерский минимальный
    h = hung(pt)
    res, indices = h._min()
    print(f"hungarian_min: {res}\n{indices}\n")

    # Венгерский максимальный
    res, indices = h._max()
    print(f"hungarian_max: {res}\n{indices}\n")

    # Жадный алгоритм
    g = gr(p_matrix=pt, steps=1)
    res, indices = g.greedy()
    print(f"greedy: {res}\n{indices}\n")

    # Жадно-бережливый алгоритм
    res, indices = g.greedy_saving()
    print(f"greedy_saving: {res}\n{indices}\n")

    # Бережливый алгоритм
    s = sv(p_matrix=pt, steps=1)
    res, indices = s.saving()
    print(f"saving: {res}\n{indices}\n")

    # Бережливо-жадный алгоритм
    res, indices = s.saving_greedy()
    print(f"saving_greedy: {res}\n{indices}")    
