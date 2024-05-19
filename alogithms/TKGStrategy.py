class TKGStrategy:
    def __init__(self, matrix, batch_count, processing_count, nu):
        self.matrix = matrix
        self.batch_count = batch_count
        self.processing_count = processing_count
        self.nu = nu

    def execute(self):
        results = []

        for k in range(1, (self.batch_count - self.nu + 2)):
            selected_rows = [False] * self.batch_count
            col_values = []
            total_sum = 0

            for col in range(self.processing_count):
                if col <= self.nu - 1:
                    col_elements = [(self.matrix[row][col], row) for row in range(self.batch_count) if not selected_rows[row]]
                    col_elements.sort()
                    value, remove_row = col_elements[k - 1]
                else:
                    max_value = float('-inf')
                    for row in range(self.batch_count):
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
        summa = max_result[1]
        col_val = max_result[0]

        return summa, col_val

# Пример использования:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
batch_count = 3
processing_count = 3
nu = 2

tkg_strategy = TKGStrategy(matrix, batch_count, processing_count, nu)
summa, col_val = tkg_strategy.execute()
print("Maximum sum:", summa)
print("Column values:", col_val)
