import numpy as np

class GkSolver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows, self.columns = matrix.shape

    def solve(self, k):
        selected_rows = [False] * self.rows
        row_indices, col_values = [], []
        total_sum = 0

        for col in range(0, self.columns, k):
            col_elements = [(self.matrix[row][col], row) for row in range(self.rows) if not selected_rows[row]]
            col_elements.sort(reverse=True)
            if (self.columns - col < k):
                k = self.columns - col
            for i in range(k):
                row_indices.append(col + i + 1)
                value = self.matrix[col_elements[i][1], col + i]
                col_values.append(value)
                selected_rows[col_elements[i][1]] = True
                total_sum += value

        return row_indices, col_values, total_sum

# Example usage:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
solver = GkSolver(matrix)
row_indices, col_values, total_sum = solver.solve(2)
print("Row Indices:", row_indices)
print("Column Values:", col_values)
print("Total Sum:", total_sum)
