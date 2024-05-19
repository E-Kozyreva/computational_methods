import numpy as np

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def TkG(self, v):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        results = []
        row_indices = [(col + 1) for col in range(columns)]

        for k in range(1, (rows - v + 2)):
            selected_rows = [False] * rows
            col_values = []
            total_sum = 0

            for col in range(columns):
                if (col <= v - 1):
                    col_elements = [(self.matrix[row][col], row) for row in range(rows) if not selected_rows[row]]
                    col_elements.sort()
                    value, remove_row = col_elements[k - 1]
                else:
                    max_value = float('-inf')
                    for row in range(rows):
                        if not selected_rows[row] and self.matrix[row][col] > max_value:
                            max_value = self.matrix[row][col]
                            remove_row = row
                    value = max_value
                selected_rows[remove_row] = True
                col_values.append(value)
                total_sum += value
            result = (col_values, total_sum)
            results.append(result)

        max_result = max(results, key=lambda x: x[1])
        return row_indices, max_result[0], max_result[1]

    def Gk(self, k):
        rows, columns = self.matrix.shape
        selected_rows = [False] * rows
        row_indices, col_values = [], []
        sum = 0

        for col in range(0, columns, k):
            col_elements = [(self.matrix[row][col], row) for row in range(rows) if not selected_rows[row]]
            col_elements.sort(reverse=True)
            if (columns - col < k):
                k = columns - col
            for i in range(k):
                row_indices.append(col + i + 1)
                value = self.matrix[col_elements[i][1], col + i]
                col_values.append(value)
                selected_rows[col_elements[i][1]] = True
                sum += value

        return row_indices, col_values, sum

# Пример использования класса
test = np.array([
    [1, 2, 3, 2, 4],
    [4, 5, 1, 1, 2],
    [1, 3, 4, 2, 3],
    [2, 1, 4, 1, 1],
    [3, 2, 2, 4, 3]
])

matrix_ops = MatrixOperations(test)

v = 3
a, b, c = matrix_ops.TkG(v)
print("TkG:", a, b, c)

k = 2
d, e, f = matrix_ops.Gk(k)
print("Gk:", d, e, f)
