import numpy as np


class CTGStrategy:
    def __init__(self, matrix, batchCount, v):
        self.matrix = matrix
        self.batchCount = batchCount
        self.v = v

    def calculate(self):
        k = np.arange(1, self.v)
        g = self.batchCount - 2 * self.v + 2 * k + 1
        t = g

        k = np.arange(self.v, 2 * self.v)
        g = self.batchCount + 2 * self.v - 2 * k
        t = np.append(t, g)

        k = np.arange(2 * self.v, self.batchCount + 1)
        g = self.batchCount - k + 1
        t = np.append(t, g) - 1

        rows_arr = np.arange(self.batchCount)
        resArr = []
        for i, j in zip(rows_arr, t):
            sortMatr = [(self.matrix[row, i], row) for row in range(self.batchCount)]
            sortMatr.sort()
            resArr.append(sortMatr[j][0])
        summa = sum(resArr)

        return summa, resArr

# Пример использования:
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

batchCount = 3
v = 2
ctg_strategy = CTGStrategy(matrix, batchCount, v)
summa, resArr = ctg_strategy.calculate()
print("Сумма:", summa)
print("Результаты:", resArr)
