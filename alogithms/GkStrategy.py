class GkStrategy:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_max_sum(self, batchCount, processingCount):
        maxSum = 0
        maxCol_val = []

        for k in range(1, batchCount + 1):
            selected_rows = [False] * batchCount
            col_values = []
            summa = 0

            for col in range(0, processingCount, k):
                col_elements = [(self.matrix[row][col], row) for row in range(batchCount) if not selected_rows[row]]
                col_elements.sort(reverse=True)
                if processingCount - col < k:
                    k = processingCount - col
                for i in range(k):
                    value = self.matrix[col_elements[i][1]][col + i]
                    col_values.append(value)
                    selected_rows[col_elements[i][1]] = True
                    summa += value

            if maxSum < summa:
                maxSum = summa
                maxCol_val = col_values

        return maxSum, maxCol_val

# Пример использования:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Пример матрицы
strategy = GkStrategy(matrix)
max_sum, max_col_val = strategy.find_max_sum(3, 3)
print("Максимальная сумма:", max_sum)
print("Значения колонок:", max_col_val)
