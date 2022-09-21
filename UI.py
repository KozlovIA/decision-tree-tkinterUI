import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import random as rnd
from backend import *


def set_matrix(set_random=False):
    while True:
        try:
            global time_limit
            matr_col = int(str(matrix_column.get()))    # кол-во столбцов и строк
            matr_row = int(str(matrix_row.get()))
            time_limit = int(str(time_limit_widget.get()))
        except:
            messagebox.showerror(title="Ошибка ввода", 
                message="Значения строк и столбцов, как и ограничение по времени должны иметь целые значения")
            return
        if matr_col > 1 and matr_col <= 10 and matr_row > 1 and matr_row <= 10:
            break
        else:
            messagebox.showerror(title="Ошибка ввода", 
                message="Значения строк и столбцов должны быть в диапазоне между отчаянием и надеждой\nМежду 1 и 11")
            return
    frame_C_matr = tk.Frame(root, width=20*matr_col, height=20+20*matr_row)#, background="#b22222")
    frame_C_matr.place(x=20, y=100)
    frame_T_matr = tk.Frame(root, width=20*matr_col, height=20+20*matr_row)#, background="#b22222")
    frame_T_matr.place(x=20, y=140+20*matr_row)
    global C_matrix, T_matrix
    C_matrix = []; T_matrix = []
    ttk.Label(frame_C_matr, text="Матрица C").place(x=0, y=0)
    ttk.Label(frame_T_matr, text="Матрица T").place(x=0, y=0)
    if set_random:
        for i in range(matr_row):
            C_matrix.append([]); T_matrix.append([])
            for j in range(matr_col):
                temp_C_matrix = tk.Label(frame_C_matr, width=3, text=rnd.randint(0, 10)); temp_C_matrix.place(x=20*j, y=20+20*i)
                C_matrix[i].append(temp_C_matrix)
                temp_T_matrix = tk.Label(frame_T_matr, width=3, text=rnd.randint(0, 10)); temp_T_matrix.place(x=20*j, y=20+20*i)
                T_matrix[i].append(temp_T_matrix)
        set_random = False
    else:
        for i in range(matr_row):
            C_matrix.append([]); T_matrix.append([])
            for j in range(matr_col):
                temp_C_matrix = tk.Entry(frame_C_matr, width=3); temp_C_matrix.place(x=20*j, y=20+20*i)
                C_matrix[i].append(temp_C_matrix)
                temp_T_matrix = tk.Entry(frame_T_matr, width=3); temp_T_matrix.place(x=20*j, y=20+20*i)
                T_matrix[i].append(temp_T_matrix)

    


def T_matrixransformation():
    global C_matrix_value, T_matrix_value
    C_matrix_value = []; T_matrix_value = []
    for i in range(len(C_matrix)):
        C_matrix_value.append([])
        T_matrix_value.append([])
        for j in range(len(C_matrix[i])):
            try:
                C_matrix_value[i].append(str(C_matrix[i][j].get()))
                T_matrix_value[i].append(str(T_matrix[i][j].get()))
            except:
                C_matrix_value[i].append(str(C_matrix[i][j].cget('text')))
                T_matrix_value[i].append(str(T_matrix[i][j].cget('text')))
    for i in range(len(C_matrix)):
        for j in range(len(C_matrix[i])):
            try:
                C_matrix_value[i][j] = int(C_matrix_value[i][j])
                T_matrix_value[i][j] = int(T_matrix_value[i][j])
            except:
                messagebox.showerror(title="Ошибка ввода", 
                    message="Значения элементов матриц должны иметь целые значения")
                return
    C1, T1 = rebase_matrix(C_matrix_value, T_matrix_value)
    C2, T2 = second_rebase(C1, T1, time_limit)
    # фреймы для вывода преобразованных матриц
    frame_C_first_rebase = tk.Frame(root, width=20*len(C_matrix[0]), height=20+20*len(C_matrix))#, background="#b22222")
    frame_C_first_rebase.place(x=40+20*len(C_matrix[0]), y=100)
    frame_T_first_rebase = tk.Frame(root, width=20*len(C_matrix[0]), height=20+20*len(T_matrix))#s, background="#b22222")
    frame_T_first_rebase.place(x=40+20*len(T_matrix[0]), y=140+20*len(C_matrix))

    #frame_C_second_rebase = tk.Frame(root, width=20*len(C_matrix[0]), height=20+20*len(C_matrix))#, background="#b22222")
    #frame_C_second_rebase.place(x=60+2*20*len(C_matrix[0]), y=100)
    #frame_T_second_rebase = tk.Frame(root, width=20*len(T_matrix[0]), height=20+20*len(T_matrix))#, background="#b22222")
    #frame_T_second_rebase.place(x=60+2*20*len(T_matrix[0]), y=140+20*len(C_matrix))    

    ttk.Label(frame_C_first_rebase, text="Матрица C первое преобразование").place(x=0, y=0)
    ttk.Label(frame_T_first_rebase, text="Матрица T первое преобразование").place(x=0, y=0)
    C_first_rebase_output = []; T_first_rebase_output = []
    for i in range(len(C_matrix_value)):
        C_first_rebase_output.append([]); T_first_rebase_output.append([])
        for j in range(len(C_matrix_value[i])):
            temp_C_matrix = tk.Label(frame_C_first_rebase, width=3, text=C_matrix_value[i][j]); temp_C_matrix.place(x=20*j, y=20+20*i)
            temp_T_matrix = tk.Label(frame_T_first_rebase, width=3, text=T_matrix_value[i][j]); temp_T_matrix.place(x=20*j, y=20+20*i)
            C_first_rebase_output[i].append(temp_C_matrix); T_first_rebase_output[i].append(temp_T_matrix)


    



root = Tk()
root.geometry('600x600+200+100')    # ширина на высоту и сколько пикселей от верха и сбоку экрана
root.title("Дерево решений")
frm = ttk.Frame(root, padding=10)   # основная рамка
frm.grid(column=10, row=10)



ttk.Label(frm, text="Введите количество строк матрицы").grid(column=0, row=0)
ttk.Label(frm, text="Введите количество столбцов матрицы").grid(column=0, row=1)
ttk.Label(frm, text="Введите ограничение по времени. По умолчанию 26").grid(column=0, row=2)
matrix_row = tk.Entry(frm); matrix_row.grid(column=1, row=0)
matrix_column = tk.Entry(frm); matrix_column.grid(column=1, row=1)
time_limit_widget = tk.Entry(frm); time_limit_widget.grid(column=1, row=2)

tk.Button(frm, text="Задать матрицу", command=set_matrix).grid(column=10, row=8)
tk.Button(frm, text="Задать матрицу со случайными числами", command=lambda: set_matrix(set_random=True)).grid(column=10, row=9)
tk.Button(frm, text="Преобразовать матрицу", command=T_matrixransformation).grid(column=10, row=10)
root.mainloop()

