import numpy as np


class ThriftyGreedyAlgorithm:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows, self.columns = matrix.shape
        self.n = self.columns // 3
        self.selected_rows = [False] * self.rows
        self.row_indices = []
        self.col_values = []
        self.sum = 0
        
    def run(self):
        for col in range(self.columns):
            self.row_indices.append(col + 1)
            value = None
            for row in range(self.rows):
                if self.selected_rows[row]:
                    continue
                if col <= self.n - 1:
                    if value is None or self.matrix[row, col] < value:
                        value = self.matrix[row, col]
                        remove_row = row
                else:
                    if value is None or self.matrix[row, col] > value:
                        value = self.matrix[row, col]
                        remove_row = row
            self.selected_rows[remove_row] = True
            self.col_values.append(value)
            self.sum += value
        
        return self.row_indices, self.col_values, self.sum

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
algorithm = ThriftyGreedyAlgorithm(matrix)
row_indices, col_values, total_sum = algorithm.run()
print("Индексы выбранных строк:", row_indices)
print("Значения выбранных столбцов:", col_values)
print("Сумма выбранных элементов:", total_sum)
