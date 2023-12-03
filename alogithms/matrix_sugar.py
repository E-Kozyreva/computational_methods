from generator.data import Vector as V
from generator.data import Matrix as M
from generator.data import PMatrix as PM


class MatrixSugar(object):

    def __init__(self, size, min_start_sugar, max_start_sugar, 
                 min_degradation, max_degradation, has_breaking):
        self.size: int = size
        self.min_start_sugar: float = min_start_sugar
        self.max_start_sugar: float = max_start_sugar
        self.min_degradation: float = min_degradation
        self.max_degradation: float = max_degradation
        self.has_breaking: bool = has_breaking
        self.a_vector = []
        self.b_matrix = []
        self.p_matrix = []


    def get_p_matrix(self) -> list:
        """Возвращает матрицу P для решения задачи оптимизации, используя заданные интервалы разброса начальных условий.
        size - размер матрицы P, has_breaking - включить/отключить поломки оборудования, file_writing - включить вывод в файл
        min_start_sugar, max_start_sugar - интервал разброса стартовых значений сахаристости (должны быть от 0 до 1!)
        min_degradation, max_degradation - коэффициенты деградации будут от min_degradation до max_degradation (должны быть от 0 до 1!)."""

        self.a_vector = V(self.size, self.min_start_sugar, self.max_start_sugar).generate_vector()
        self.b_matrix = M(self.size, self.size + 1, self.min_degradation, self.max_degradation).generate_matrix()
        self.p_matrix = PM(self.a_vector, self.b_matrix, self.has_breaking).generate_p_matrix()

        return self.p_matrix
