class Greedy(object):

    def __init__(self, p_matrix: list, steps: int = 0):
        self.p_matrix = p_matrix
        self.steps = steps
        self.result = 0
        self.indices = []
        self.took = []


    def greedy(self) -> tuple:
        """Возвращает результат и список-перестановку целевой функции, поиск результата с помощью жадного алгоритма."""
        col_max_index = 0
        for j in range(len(self.p_matrix)):
            col_max = 0
            for i in range(len(self.p_matrix)):
                is_took = False

                for k in range(len(self.took)):
                    if self.took[k] == i:
                        is_took = True
                        break

                if is_took:
                    continue

                if self.p_matrix[i][j] > col_max:
                    col_max = self.p_matrix[i][j]
                    col_max_index = i
            self.result += col_max
            self.indices.append(col_max_index)
            self.took.append(col_max_index)
        return self.result, self.indices
    

    def greedy_saving(self) -> tuple:
        """Возвращает результат и список-перестановку целевой функции, поиск результата с помощью бережливо-жадного алгоритма.\n
            saving_steps - количество шагов в режиме сбережения, далее будет жадный режим."""
        saving_steps_completed = 0

        for j in range(len(self.p_matrix)):
            col_max_index, col_min_index = 0, 0
            col_min, col_max = 10, 0
            saving_mode = saving_steps_completed < self.steps

            for i in range(len(self.p_matrix)):
                is_took = False

                for k in range(len(self.took)):
                    if self.took[k] == i:
                        is_took = True
                        break

                if is_took:
                    continue

                if saving_mode and self.p_matrix[i][j] < col_min:
                    col_min = self.p_matrix[i][j]
                    col_min_index = i

                if not saving_mode and self.p_matrix[i][j] > col_max:
                    col_max = self.p_matrix[i][j]
                    col_max_index = i

            if saving_mode:
                self.result += col_min
                self.indices.append(col_min_index)
                self.took.append(col_min_index)
            else:
                self.result += col_max
                self.indices.append(col_max_index)
                self.took.append(col_max_index)

            saving_steps_completed += 1

        return self.result, self.indices
