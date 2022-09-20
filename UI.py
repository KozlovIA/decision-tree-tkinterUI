import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import random as rnd


def set_matrix(set_random=False):
    try:
        matr_col = int(str(matrix_column.get()))    # кол-во столбцов и строк
        matr_row = int(str(matrix_row.get()))
    except:
        messagebox.showerror(title="Ошибка ввода", 
            message="Значения строк и столбцов должны иметь целые значения")
        return

    frame_matrix = tk.Frame(root, width=20*matr_col, height=20*matr_row)#, background="#b22222")
    frame_matrix.place(x=20, y=100)
    global matrix
    matrix = []
    if set_random:
        for i in range(matr_row):
            matrix.append([])
            for j in range(matr_col):
                temp_matrix = tk.Label(frame_matrix, width=3, text=rnd.randint(0, 10)); temp_matrix.place(x=20*i, y=20*j)
                matrix[i].append(temp_matrix)
        set_random = False
    else:
        for i in range(matr_row):
            matrix.append([])
            for j in range(matr_col):
                temp_matrix = tk.Entry(frame_matrix, width=3); temp_matrix.place(x=20*i, y=20*j)
                matrix[i].append(temp_matrix)

    


def matrix_transformation():
    matrix_value = []
    for i in range(len(matrix)):
        matrix_value.append([])
        for j in range(len(matrix[i])):
            try:
                matrix_value[i].append(str(matrix[i][j].get()))
            except:
                matrix_value[i].append(str(matrix[i][j].cget('text')))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            try:
                matrix_value[i][j] = int(matrix_value[i][j])
            except:
                messagebox.showerror(title="Ошибка ввода", 
                    message="Значения элементов матрицы должны иметь целые значения")
                return
    print(matrix_value)


root = Tk()
root.geometry('600x400+200+100')    # ширина на высоту и сколько пикселей от верха и сбоку экрана
root.title("Дерево решений")
frm = ttk.Frame(root, padding=10)   # основная рамка
frm.grid(column=10, row=10)



ttk.Label(frm, text="Программа для построения дерева решений").grid(column=0, row=0)
ttk.Label(frm, text="Введите количество строк матрицы").grid(column=0, row=1)
ttk.Label(frm, text="Введите количество столбцов матрицы").grid(column=0, row=2)
matrix_row = tk.Entry(frm); matrix_row.grid(column=1, row=1)
matrix_column = tk.Entry(frm); matrix_column.grid(column=1, row=2)

tk.Button(frm, text="Задать матрицу", command=set_matrix).grid(column=10, row=8)
tk.Button(frm, text="Задать матрицу со случайными числами", command=lambda: set_matrix(set_random=True)).grid(column=10, row=9)
tk.Button(frm, text="Преобразовать матрицу", command=matrix_transformation).grid(column=10, row=10)
root.mainloop()

