class TkG:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.row_indices = [(col + 1) for col in range(self.columns)]

    def calculate(self, v):
        results = []

        for k in range(1, (self.rows - v + 2)):
            selected_rows = [False] * self.rows
            col_values = []
            total_sum = 0

            for col in range(self.columns):
                if (col <= v - 1):
                    col_elements = [(self.matrix[row][col], row) for row in range(self.rows) if not selected_rows[row]]
                    col_elements.sort()
                    value, remove_row = col_elements[k - 1]
                else:
                    max_value = float('-inf')
                    for row in range(self.rows):
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
        return self.row_indices, max_result[0], max_result[1]


# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tkg_instance = TkG(matrix)
row_indices, col_values, total_sum = tkg_instance.calculate(2)

print("Row Indices:", row_indices)
print("Column Values:", col_values)
print("Total Sum:", total_sum)
