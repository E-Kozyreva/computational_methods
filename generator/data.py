class Vector:

    def __init__(self, n: int, _min: float, _max: float):
        self.n = n
        self._min = _min
        self._max = _max
        self.vector = []


    def generate_vector(self) -> list:
        """Возвращает список размера n со случайными значениями от _min до _max."""
        from random import uniform
        self.vector = [uniform(self._min, self._max) for i in range(self.n)]
        return self.vector


class Matrix:

    def __init__(self, _str: int, _col: int, _min: float, _max: float):
        self._str = _str
        self._col = _col
        self._min = _min
        self._max = _max
        self.matrix = []

    
    def generate_matrix(self) -> list:
        """Возвращает двумерный список размера (_str)x(_col) со случайными значениями от _min до _max."""
        from random import uniform
        self.matrix = [[uniform(self._min, self._max) for j in range(self._col)] for i in range(self._str)]
        return self.matrix


class PMatrix:
    
    def __init__(self, a_vector: list, b_matrix: list, has_breaking: bool):
        self.a_vector = a_vector
        self.b_matrix = b_matrix
        self.has_breaking = has_breaking
        self.p_matrix = []


    def generate_p_matrix(self) -> list:
        """Возвращает матрицу P для решения задачи оптимизации (Элементы в ней не могут быть больше 1).
           a_vector - вектор стартовых значений сахаристости размера n,
           b_matrix - матрица деградации размера (n)x(n+1)
           has_breaking - были ли поломки оборудования."""
        self.p_matrix = []
        n = len(self.a_vector)
        break_1_day, break_2_day = 1, n // 2 + 1

        for i in range(n):
            _str = [self.a_vector[i]]
            day, work_day = 0, 0

            while work_day < n - 1:
                res = _str[work_day] * self.b_matrix[i][day]

                if day == break_1_day and self.has_breaking:
                    res *= self.b_matrix[i][day]
                    day += 1

                if day == break_2_day and self.has_breaking:
                    res *= self.b_matrix[i][day]
                    day += 1

                _str.append(res)
                work_day += 1
                day += 1

            self.p_matrix.append(_str)

        return self.p_matrix
