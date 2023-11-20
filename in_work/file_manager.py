import os
filename: str


def create():
    global filename

    file_number = 1
    while os.path.exists("test_" + str(file_number) + ".txt"):
        file_number += 1

    filename = "test_" + str(file_number) + ".txt"

    file = open(file=filename, mode='w', encoding='utf-8')
    file.close()


def write_start_conditions(a_vector, b_matrix):
    file = open(file=filename, mode='a', encoding='utf-8')
    file.write("Исходные условия (Стартовая сахаристость | Матрица деградации)\n")

    for i in range(len(a_vector)):
        file.write("{:.4}".format(a_vector[i]))
        file.write(' | ')

        for j in range(len(b_matrix[0])):
            file.write("{:.4}".format(b_matrix[i][j]))
            file.write(' ')
        file.write('\n')

    file.write('\n')
    file.close()


def write_sugar_matrix(p_matrix):
    file = open(file=filename, mode='a', encoding='utf-8')
    file.write("Матрица сахаристости\n")

    for i in range(len(p_matrix)):
        _str = p_matrix[i]

        for j in range(len(_str)):
            file.write("{:.4}".format(p_matrix[i][j]))
            file.write(' ')
        file.write('\n')

    file.write('\n')
    file.close()


def write_algorithm_res(alg_name, result, indices):
    file = open(file=filename, mode='a', encoding='utf-8')
    file.write(alg_name + ': Результат = ')
    file.write("{:.4}".format(result))
    file.write(". Индексы: ")

    for i in range(len(indices)):
        file.write(str(indices[i]) + ', ')

    file.write('\n')
    file.close()
