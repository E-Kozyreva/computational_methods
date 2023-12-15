import numpy as np
import time
from scipy.optimize import linear_sum_assignment


class Hungarian(object):

    def __init__(self, p_matrix: list):
        self.p_matrix = p_matrix
        self.min_result = 0
        self.max_result = 0
        self.max_elem = np.max(self.p_matrix)
        self.reverse_p_matrix = np.copy(self.p_matrix)


    def _min(self) -> tuple:
        """Возвращает результат и список-перестановку целевой функции, поиск худшего результата с помощью венгерского алгоритма."""
        start = time.time()
        row_indices, col_indices = linear_sum_assignment(self.p_matrix)

        self.min_result = [self.p_matrix[row_indices[i]][col_indices[i]] for i in range(len(row_indices))]

        for i in range(len(row_indices)):
            row_indices[col_indices[i]] = i
        end = time.time()

        wfile = open("time/hungarian_min.txt", "a")
        wfile.write(f"{end - start}\n")

        return self.min_result, row_indices
    

    def _max(self) -> tuple:
        """Возвращает результат и список-перестановку целевой функции, поиск лучшего результата с помощью венгерского алгоритма."""
        start = time.time()
        for i in range(len(self.p_matrix)):
            for j in range(len(self.p_matrix)):
                self.reverse_p_matrix[i][j] = -1 * self.p_matrix[i][j] + self.max_elem

        row_indices, col_indices = linear_sum_assignment(self.reverse_p_matrix)

        self.max_result = [self.p_matrix[row_indices[i]][col_indices[i]] for i in range(len(row_indices))]

        for i in range(len(row_indices)):
            row_indices[col_indices[i]] = i
        end = time.time()
        
        wfile = open("time/hungarian_max.txt", "a")
        wfile.write(f"{end - start}\n")

        return self.max_result, row_indices
