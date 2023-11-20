from alogithms.matrix_sugar import MatrixSugar as ms
from alogithms.hungarian import Hungarian as hung
from alogithms.greedy import Greedy as gr
from alogithms.saving import Saving as sv
import file_manager as fm


if __name__ == '__main__':

    pt = ms(size=8, min_start_sugar=1, max_start_sugar=1,
           min_degradation=0.7, max_degradation=0.7, has_breaking=True).get_p_matrix()
    
    pf = ms(size=8, min_start_sugar=1, max_start_sugar=1,
            min_degradation=0.7, max_degradation=0.7, has_breaking=False).get_p_matrix()


    # Венгерский минимальный
    res, indices = hung._min(pt)
    print(f"hungarian_min: {res}\n{indices}\n\n")

    # Венгерский максимальный
    res, indices = hung._max(pt)
    print(f"hungarian_max: {res}\n{indices}\n\n")

    # Жадный алгоритм
    res, indices = gr.greedy(pt)
    print(f"greedy: {res}\n{indices}\n\n")

    # Жадно-бережливый алгоритм
    res, indices = gr.greedy_saving(pt, 1)
    print(f"greedy_saving: {res}\n{indices}\n\n")

    # Бережливый алгоритм
    res, indices = sv.saving(pt)
    print(f"saving: {res}\n{indices}\n\n")

    # Бережливо-жадный алгоритм
    res, indices = sv.saving_greedy(pt, 1)
    print(f"saving_greedy: {res}\n{indices}\n\n")    
