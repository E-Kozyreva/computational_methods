import string
from tkinter import *
from tkinter import ttk

import matplotlib

import alogithms.algorithms as algs
import matplotlib.pyplot as plt

import file_manager as fm

matrix_entries = []


def run_experiments():
    experiments_quantity = int(experiments_quantity_entry.get())
    n = int(n_entry.get())

    hung_max_avg = []
    for i in range(n):
        hung_max_avg.append(0)

    hung_min_avg = []
    for i in range(n):
        hung_min_avg.append(0)

    greedy_avg = []
    for i in range(n):
        greedy_avg.append(0)

    saving_avg = []
    for i in range(n):
        saving_avg.append(0)

    gre_sav_avg = []
    for i in range(n):
        gre_sav_avg.append(0)

    sav_gre_avg = []
    for i in range(n):
        sav_gre_avg.append(0)

    steps = []
    for i in range(int(n)):
        steps.append(i+1)

    for k in range(experiments_quantity):
        p_matrix = algs.get_p_matrix_sugar(size=int(n_entry.get()),
                                           has_breaking=breaks_val.get(),
                                           file_writing=False,
                                           min_start_sugar=float(start_sugar_from_entry.get()),
                                           max_start_sugar=float(start_sugar_to_entry.get()),
                                           min_degradation=float(degradation_from_entry.get()),
                                           max_degradation=float(degradation_to_entry.get()))


        values = []


        # Венгерский (max)
        value, indices = algs.hungarian_max(p_matrix)
        for i in range(len(indices)):
            if i == 0:
                values.append(p_matrix[indices[i]][i])
            if i != 0:
                values.append(values[i - 1] + p_matrix[indices[i]][i])
            hung_max_avg[i] += values[i]
        values.clear()

        # Венгерский (min)
        value, indices = algs.hungarian_min(p_matrix)
        for i in range(len(indices)):
            if i == 0:
                values.append(p_matrix[indices[i]][i])
            if i != 0:
                values.append(values[i - 1] + p_matrix[indices[i]][i])
            hung_min_avg[i] += values[i]
        values.clear()

        # Бережливый
        value, indices = algs.saving(p_matrix)
        for i in range(len(indices)):
            if i == 0:
                values.append(p_matrix[indices[i]][i])
            if i != 0:
                values.append(values[i - 1] + p_matrix[indices[i]][i])
            saving_avg[i] += values[i]
        values.clear()

        # Жадный
        value, indices = algs.greedy(p_matrix)
        for i in range(len(indices)):
            if i == 0:
                values.append(p_matrix[indices[i]][i])
            if i != 0:
                values.append(values[i - 1] + p_matrix[indices[i]][i])
            greedy_avg[i] += values[i]
        values.clear()

        # Жадно-бережливый
        value, indices = algs.greedy_saving(p_matrix, len(p_matrix) / 2)
        for i in range(len(indices)):
            if i == 0:
                values.append(p_matrix[indices[i]][i])
            if i != 0:
                values.append(values[i - 1] + p_matrix[indices[i]][i])
            gre_sav_avg[i] += values[i]
        values.clear()

        # Бережливо-жадный
        value, indices = algs.saving_greedy(p_matrix, len(p_matrix) / 2)
        for i in range(len(indices)):
            if i == 0:
                values.append(p_matrix[indices[i]][i])
            if i != 0:
                values.append(values[i - 1] + p_matrix[indices[i]][i])
            sav_gre_avg[i] += values[i]
        values.clear()

    for i in range(n):
        hung_max_avg[i] /= experiments_quantity
        hung_min_avg[i] /= experiments_quantity
        greedy_avg[i] /= experiments_quantity
        saving_avg[i] /= experiments_quantity
        sav_gre_avg[i] /= experiments_quantity
        gre_sav_avg[i] /= experiments_quantity


    plt.plot(steps, hung_max_avg, label="Венгерский (max)")
    plt.plot(steps, hung_min_avg, label="Венгерский (min)")
    plt.plot(steps, greedy_avg, label="Жадный")
    plt.plot(steps, saving_avg, label="Бережливый")
    plt.plot(steps, sav_gre_avg, label="Бережливо-жадный")
    plt.plot(steps, gre_sav_avg, label="Жадно-бережливый")

    plt.title("Усредненные результаты серии экспериментов")
    plt.xlabel('Этапы переработки')
    plt.ylabel('Результат (S)')
    plt.legend()
    plt.show()


def run_one_experiment():
    steps = []
    values = []

    p_matrix = algs.get_p_matrix_sugar(size=int(n_entry.get()),
                                       has_breaking=breaks_val.get(),
                                       file_writing=writing_val,
                                       min_start_sugar=float(start_sugar_from_entry.get()),
                                       max_start_sugar=float(start_sugar_to_entry.get()),
                                       min_degradation=float(degradation_from_entry.get()),
                                       max_degradation=float(degradation_to_entry.get()))

    # Венгерский (max)
    value, indices = algs.hungarian_max(p_matrix)
    for i in range(len(indices)):
        steps.append(i + 1)
        if i == 0:
            values.append(p_matrix[indices[i]][i])
        if i != 0:
            values.append(values[i-1] + p_matrix[indices[i]][i])

    if writing_val:
        fm.write_algorithm_res(alg_name='Венгерский (max)', result=value, indices=indices)

    plt.plot(steps, values, label="Венгерский (max)")
    steps.clear()
    values.clear()

    # Венгерский (min)
    value, indices = algs.hungarian_min(p_matrix)
    for i in range(len(indices)):
        steps.append(i + 1)
        if i == 0:
            values.append(p_matrix[indices[i]][i])
        if i != 0:
            values.append(values[i - 1] + p_matrix[indices[i]][i])

    if writing_val:
        fm.write_algorithm_res(alg_name='Венгерский (min)', result=value, indices=indices)

    plt.plot(steps, values, label="Венгерский (min)")
    steps.clear()
    values.clear()

    # Бережливый
    value, indices = algs.saving(p_matrix)
    for i in range(len(indices)):
        steps.append(i + 1)
        if i == 0:
            values.append(p_matrix[indices[i]][i])
        if i != 0:
            values.append(values[i - 1] + p_matrix[indices[i]][i])

    if writing_val:
        fm.write_algorithm_res(alg_name='Бережливый', result=value, indices=indices)

    plt.plot(steps, values, label="Бережливый")
    steps.clear()
    values.clear()

    # Жадный
    value, indices = algs.greedy(p_matrix)
    for i in range(len(indices)):
        steps.append(i + 1)
        if i == 0:
            values.append(p_matrix[indices[i]][i])
        if i != 0:
            values.append(values[i - 1] + p_matrix[indices[i]][i])

    if writing_val:
        fm.write_algorithm_res(alg_name='Жадный', result=value, indices=indices)

    plt.plot(steps, values, label="Жадный")
    steps.clear()
    values.clear()

    # Жадно-бережливый
    value, indices = algs.greedy_saving(p_matrix, len(p_matrix) / 2)
    for i in range(len(indices)):
        steps.append(i + 1)
        if i == 0:
            values.append(p_matrix[indices[i]][i])
        if i != 0:
            values.append(values[i - 1] + p_matrix[indices[i]][i])

    if writing_val:
        fm.write_algorithm_res(alg_name='Жадно-бережливый', result=value, indices=indices)

    plt.plot(steps, values, label="Жадно-бережливый")
    steps.clear()
    values.clear()

    # Бережливо-жадный
    value, indices = algs.saving_greedy(p_matrix, len(p_matrix) / 2)
    for i in range(len(indices)):
        steps.append(i + 1)
        if i == 0:
            values.append(p_matrix[indices[i]][i])
        if i != 0:
            values.append(values[i - 1] + p_matrix[indices[i]][i])

    if writing_val:
        fm.write_algorithm_res(alg_name='Бережливо-жадный', result=value, indices=indices)

    plt.plot(steps, values, label="Бережливо-жадный")
    steps.clear()
    values.clear()



    plt.title("Результаты одного эксперимента")
    plt.xlabel('Этапы переработки')
    plt.ylabel('Результат (S)')
    plt.legend()
    plt.show()


root = Tk()


root['bg'] = '#fafafa'
root.geometry("1000x600")


frame = ttk.Frame()
frame.pack(fill=BOTH, expand=True, )

Label(frame, text="Количество партий:", bg='#fafafa', font="Times 13").place(x=50, y=40)
n_entry = Entry(frame, width=5, font="Times 14", bg='#edf5f3')
n_entry.place(x=220, y=40)

Label(frame, text="Интервал стартовой сахаристости (значения в полях от 0 до 1):", bg='#fafafa', font="Times 13").place(x=50, y=70)
start_sugar_from_entry = Entry(frame, width=5, font="Times 14", bg='#edf5f3')
start_sugar_from_entry.place(x=520, y=70)
start_sugar_to_entry = Entry(frame, width=5, font="Times 14", bg='#edf5f3')
start_sugar_to_entry.place(x=570, y=70)
Label(frame, text="Интервал коэффициентов деградации (значения в полях от 0 до 1):", bg='#fafafa', font="Times 13").place(x=25, y=100)
degradation_from_entry = Entry(frame, width=5, font="Times 14", bg='#edf5f3')
degradation_from_entry.place(x=520, y=100)
degradation_to_entry = Entry(frame, width=5, font="Times 14", bg='#edf5f3')
degradation_to_entry.place(x=570, y=100)

breaks_val = BooleanVar()
Label(frame, text="Включить поломки оборудования:", bg='#fafafa', font="Times 13").place(x=25, y=130)
breaks_check_button = Checkbutton(frame, variable=breaks_val)
breaks_check_button.place(x=300, y=130)

writing_val = BooleanVar()
Label(frame, text="Вывести результаты в файл:", bg='#fafafa', font="Times 13").place(x=75, y=160)
info_check_button = Checkbutton(frame, variable=writing_val)
info_check_button.place(x=300, y=160)


Label(frame, text="Количество экспериментов:", bg='#fafafa', font="Times 13")\
    .place(x=70, y=320)
experiments_quantity_entry = Entry(frame, width=7, font="Times 14", bg='#edf5f3')
experiments_quantity_entry.place(x=290, y=320)

Button(frame, text="Провести серию экспериментов", font="Times 14", command=run_experiments).place(x=390, y=310)


Button(frame, text="Провести эксперимент", font="Times 14", command=run_one_experiment).place(x=200, y=200)

matplotlib.use('TkAgg')
root.mainloop()




